$(function() {
   $('#instructions').instructions({'onfinish': function() {
       window.location.href = practice_path;
   }});
   
   $('#practice').meditime_practice();
});

(function($) {
    $.fn.instructions = function(options) {
        var me = $(this);
        
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
            if (should_advance(evt.keyCode)) {
                advance();
            }
        });
        
    }
})(jQuery);

(function($) {
    $.fn.meditime_practice = function(options) {
        var me = this;
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
            'status_container' : '#practice'
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
            console.log("I'm in start")
            pvt.change_state('running');
            pvt.show_status('running');
        };
        
        pvt.finish = function() {
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
            console.log("run_state: "+pvt.run_state+" -> "+new_state);
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
            
            console.log("Handling "+key);
            console.log("Target key: "+tk);
            
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
                pvt.change_state('finished');
                pvt.show_status('success');
            }
            // And we can just fall through.
        }
        
        $(document).keydown(function(evt) {
            var keyChar = String.fromCharCode(evt.keyCode);
            console.log("Handling key "+keyChar+" in state "+pvt.run_state);
            switch(pvt.run_state) {
            case 'stopped':
                console.log("Looking for "+pvt.settings.count_key);
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
                    pvt.change_state("stopped");
                    pvt.show_status("getready");
                }
                break;
            case 'finished':
                break;
            default:
                alert("Whoah! I'm somehow in state: "+pvt.run_state);
            }
        });
        pvt.reset();
    }
})(jQuery);