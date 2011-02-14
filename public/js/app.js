$(function() {
   $('#instructions').instructions({'onfinish': function() {
       window.location.href = practice_path;
   }});
   
   $('#practice').meditime_practice({'onfinish': function() {
       window.location.href = next_page;
   }});
   
   $('#meditime_run').meditime_run();
});

(function($) {
    $.fn.meditime_run = function(options) {
        var me = $(this);
        // Ensure we're not going to operate on non-matching pages.
        if (me.size() !== 1) {
            return;
        }

        var pvt = {};
        pvt.settings = $.extend({
            'save_path' : '',
            'start_key' : 'A',
            'run_ms' : (60*1000*15),
            'onfinish' : function() {},
            'status_container' : '#meditime_run'
        });
        pvt.settings.start_key = pvt.settings.start_key.toUpperCase();

        pvt.reset = function() {
            pvt.presses = new Array();
            pvt.times = new Array();
            pvt.save_queue = {};
            pvt.run_state = 'stopped';
            pvt.show_status('getready');
        }

        pvt.show_status = function(name) {
            $(pvt.settings.status_container).children().hide();
            $('#'+name).show();
        }

        pvt.start = function() {
            pvt.run_state = 'running';
            pvt.start_time = new Date();
            pvt.show_status('running');
        }

        pvt.handle_key = function(key) {
            var time = new Date() - pvt.start_time;
            var idx = pvt.presses.length;
            pvt.presses.push(key);
            pvt.times.push(time);
            pvt.save_queue[idx] = {
                'num' : idx,
                'key' : key,
                'time' : time,
                'finish' : false
            };
            if (time > pvt.settings.run_ms) {
                pvt.save_queue[idx].finish = true;
                pvt.run_state = 'finished';
                pvt.onfinish();
            }
            $.ajax('', {
                'type' : 'POST',
                'data' : pvt.save_queue,
                'dataType' : 'json'
            }).success(function(a, b, c) {
                console.log("I'm in success.")
                console.log(a);
            })
            console.log(pvt.save_queue);
        }

        pvt.handle_response = function(resp) {
            // Find out what IDs we should delete. Delete 'em.
        }

        pvt.reset();

        $(document).keydown(function(evt) {
            var keyChar = String.fromCharCode(evt.keyCode);
            switch(pvt.run_state) {
            case 'stopped':
                if (keyChar === pvt.settings.start_key) {
                    pvt.start();
                    pvt.handle_key(keyChar);
                }
                break;
            case 'running':
                pvt.handle_key(keyChar);
                break;
            
            default:
                alert("Oops! I'm somehow in state: "+pvt.run_state);
                break;
            }
        });
    }
})(jQuery);

(function($) {
    $.fn.instructions = function(options) {
        var me = $(this);
        if (me.size() !== 1) {
            return;
        }
        
        var settings = $.extend({
            'key_map' : {"SPACEBAR" : 32, "a" : 65, "f" : 70},
            'show_idx' : 0,
            'onfinish' : function() {}
        }, options);
        
        var show_idx = settings.show_idx;

        var show = function(idx) {
            me.children('li').hide();
            $(me.children('li')[idx]).show();
        };
        
        var get_step = function(idx) {
            return $(me.children('li')[idx]);
        }
        
        var get_step_advancer = function(step) {
            return step.find('code:last').text();
        }
        
        var should_advance = function(keycode) {
            var advancer = get_step_advancer(get_step(show_idx));
            var adv_keycode = settings.key_map[advancer];
            return (adv_keycode === keycode);
        }
        
        var advance = function() {
            show_idx++;
            if (show_idx >= me.children('li').size()) {
                settings.onfinish();
            } else {
                show(show_idx);
            }
        }

        show(show_idx);

        // The main event! See if we can advance and do so.
        $(document).keydown(function(evt) {
            console.log("hug");
            if (should_advance(evt.keyCode)) {
                advance();
            }
        });
        
    }
})(jQuery);

(function($) {
    $.fn.meditime_practice = function(options) {
        var me = this;
        if (me.size() !== 1) {
            return;
        }
        
        var pvt = {};
        pvt.settings = $.extend({
            'cycle_length': 9,
            'count_key' : 'A',
            'reset_key' : 'F',
            'restart_key' : ' ',
            'practice_cycles' : 1.5,
            'debounce_ms' : 300,
            'min_avg_ms' : 1500,
            'max_avg_ms' : 30000,
            'status_container' : '#practice',
            'onfinish' : function() {}
        }, options);
        // Keycodes get converted to upper-case strings.
        pvt.settings.count_key = pvt.settings.count_key.toUpperCase();
        pvt.settings.reset_key = pvt.settings.reset_key.toUpperCase();
        pvt.settings.restart_key = pvt.settings.restart_key.toUpperCase();
        
        pvt.reset = function() {
            pvt.presses = new Array();
            pvt.times = new Array();
            pvt.run_state = 'stopped';
            pvt.iters = Math.floor(
                pvt.settings.cycle_length*pvt.settings.practice_cycles);
            pvt.show_status('getready');
        }
        
        pvt.start = function() {
            pvt.change_state('running');
            pvt.show_status('running');
        };
        
        pvt.finish = function() {
            // Ensure our average time is OK...
            if (pvt.fails_timing(pvt.times)) {
                pvt.throw_error('err_timing');
                return;
            }
            pvt.change_state('finished');
            pvt.show_status('success');
        }
        
        pvt.throw_error = function(err_name) {
            pvt.change_state('error');
            pvt.show_status(err_name);
        }
        
        pvt.show_status = function(name) {
            $(pvt.settings.status_container).children().hide();
            $('#'+name).show();
        }
        
        pvt.change_state = function(new_state) {
            pvt.run_state = new_state;
        }
        
        pvt.target_key = function() {
            var idx = ((pvt.presses.length+1) % pvt.settings.cycle_length);
            if (idx === 0) {
                return pvt.settings.reset_key;
            } else {
                return pvt.settings.count_key;
            }
        }
        
        pvt.fails_timing = function(times) {
            var len = times.length;
            var total_time = times[len-1] - times[0];
            var avg_time = total_time / len;
            if (avg_time < pvt.settings.min_avg_ms) {
                return true;
            }
            if (avg_time > pvt.settings.max_avg_ms) {
                return true;
            }
            return false;
        }
        
        pvt.fails_debounce = function(time_arr) {
            var len = time_arr.length;
            if (len < 2) {
                return false;
            }
            var time_delta = time_arr[len-1] - time_arr[len-2];
            return (time_delta < pvt.settings.debounce_ms);
        }
        
        pvt.handle_key_run = function(key) {
            // Shorthand to save typing
            var tk = pvt.target_key();
            var ck = pvt.settings.count_key;
            var rk = pvt.settings.reset_key;
            
            
            if (tk === key) {
                pvt.presses.push(key);
                pvt.times.push(new Date());
            } else {
                // It's some kind of error.
                if (key === ck) {
                    // Too many counts
                    pvt.throw_error('err_too_many');
                    return;
                } else if (key === rk) {
                    // too few counts
                    pvt.throw_error('err_too_few');
                    return;
                } else {
                    // wrong key entirely
                    pvt.throw_error('err_wrong_key');
                    return;
                }
            }
            
            // One final error: debounce!
            if (pvt.fails_debounce(pvt.times)) {
                pvt.throw_error('err_debounce');
                return;
            }
            // Finally, if we've got enough, we have success!
            if (pvt.presses.length >= pvt.iters) {
                pvt.finish();
            }
            // And we can just fall through. Overall timing errors will be
            // caught in finish()
        }
        
        $(document).keydown(function(evt) {
            var keyChar = String.fromCharCode(evt.keyCode);
            switch(pvt.run_state) {
            case 'stopped':
                if (keyChar === pvt.settings.count_key) {
                    pvt.start();
                    pvt.handle_key_run(keyChar);
                }
                break;
            case 'running':
                pvt.handle_key_run(keyChar);
                break;
            case 'error':
                if (keyChar === pvt.settings.restart_key) {
                    pvt.reset();
                }
                break;
            case 'finished':
                if (keyChar === pvt.settings.restart_key) {
                    pvt.settings.onfinish();
                }
                break;
            default:
                alert("Oops! I'm somehow in state: "+pvt.run_state);
            }
        });
        pvt.reset();
    }
})(jQuery);