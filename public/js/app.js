if (!window.console) {
    window.console = {};
    window.console.log = function() {};
}

$(function() {
    $('#instructions').instructions(
        {'onfinish': data.nav_practice });

    $('#guided_practice').meditime_practice(
        {
            'onfinish': data.nav_run,
            'guide': '#practice_guide',
            'status_container': '#guided_practice',
            'log_path': data.log_path,
            'flasher' : '#flasher'
    });

    $('#practice').meditime_practice(
        {
            'onfinish': data.nav_run,
            'log_path': data.log_path,
            'flasher' : '#flasher'
    });

    $('#meditime_run').meditime_run(
        { 
            'onfinish': data.nav_thanks,
            'flasher' : '#flasher'
    });
});

(function($){
    $.fn.flashable = function(options) {
        var pvt = {};
        pvt.settings = $.extend({
            'duration' : 300,
            'color' : "#f4e9d5",
            }, options);

        pvt.flash_fx = function(elt) {
            $(this).effect(
                "highlight",
                {"color": pvt.settings.color}, 
                pvt.settings.duration);
            }

            this.each(function() {
                this.flash = pvt.flash_fx;
        });
    }
})(jQuery);

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
        }, options);
        pvt.settings.start_key = pvt.settings.start_key.toUpperCase();
        $(pvt.settings.flasher).flashable();

        pvt.reset = function() {
            pvt.currently_pressed = {};
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
        
        pvt.flash = function() {
            if ($(pvt.settings.flasher)) {
                $(pvt.settings.flasher).each(function() {
                    this.flash();
                });
            }
        }

        pvt.start = function() {
            pvt.run_state = 'running';
            pvt.start_time = new Date();
            pvt.show_status('running');
        }

        pvt.handle_key = function(key) {
            var pair = pvt.currently_pressed[key];
            var since_run_start = pair.keydown.timeStamp - pvt.start_time;
            var duration = pair.keyup.timeStamp - pair.keydown.timeStamp;
            var idx = pvt.presses.length;
            pvt.presses.push(key);
            pvt.times.push(since_run_start);
            pvt.save_queue[idx] = {
                'num' : idx,
                'key' : key,
                'since_run_start' : since_run_start,
                'duration' : duration,
                'timezone_offset_min' : new Date().getTimezoneOffset()
            };
            $.ajax('', {
                'type' : 'POST',
                'data' : {'save_queue' : JSON.stringify(pvt.save_queue)},
                'dataType' : 'json'
            }).success(function(data) {
                var saved_nums = data.saved_nums;
                for (var i = 0; i < saved_nums.length; i++) {
                    delete pvt.save_queue[saved_nums[i]];
                }
                if (data['finish']) {
                    pvt.settings.onfinish();
                }
            });
            // And ensure we don't see this again.
            delete pvt.currently_pressed[key];
        }

        pvt.reset();

        $(document).keydown(function(evt) {
            var keyChar = String.fromCharCode(evt.keyCode);
            // Don't re-process keydowns we already have.
            if (pvt.currently_pressed[keyChar]) { 
                console.log("Not re-processing "+keyChar);
                return; 
            }
            console.log(evt);
            
            switch(pvt.run_state) {
            case 'stopped':
                if (keyChar === pvt.settings.start_key) {
                    pvt.start();
                    pvt.flash();
                    pvt.currently_pressed[keyChar] = {'keydown': evt};
                }
                break;
            case 'running':
                pvt.flash();
                pvt.currently_pressed[keyChar] = {'keydown': evt};
                // We'll handle sending this to the server on keyup().
                break;
            case 'finished':
                // Don't worry about keys in this case. Shouldn't happen
                // but not an error if it does.
                break;
            
            default:
                alert("Oops! I'm somehow in state: "+pvt.run_state);
                break;
            }
        });
        
        $(document).keyup(function(evt) {
            console.log(evt);
            var keyChar = String.fromCharCode(evt.keyCode);
            // We *must* be waiting on a keyup for this processing to make
            if (!pvt.currently_pressed[keyChar]) { 
                console.log("Got an unexpected keyup for "+keyChar);
                return; 
            }
            pvt.currently_pressed[keyChar]['keyup'] = evt;
            pvt.handle_key(keyChar);
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
            'key_map' : {"SPACEBAR" : 32, "A" : 65, "F" : 70},
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
            return step.find('code:last').text().toUpperCase();
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
        if (me.size() !== 1) {
            return;
        }
        
        var pvt = {};
        pvt.settings = $.extend({
            'cycle_length': 9,
            'count_key' : 'A',
            'reset_key' : 'F',
            'restart_key' : 'A',
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
        $(pvt.settings.flasher).flashable();
        
        pvt.reset = function() {
            pvt.presses = new Array();
            pvt.times = new Array();
            pvt.run_state = 'stopped';
            pvt.iters = Math.floor(
                pvt.settings.cycle_length*pvt.settings.practice_cycles);
            pvt.build_keyguide(pvt.iters);
            pvt.show_status('getready');
            pvt.currently_pressed = {};
        }
        
        pvt.send_log = function(key) {
            var lp = pvt.settings.log_path;
            if (!lp) { return; }
            var prefix = pvt.settings.status_container.replace("#", '');
            var full_path = lp+prefix+"_"+key;
            $.ajax(full_path, {});
        }
        
        pvt.flash = function() {
            if ($(pvt.settings.flasher)) {
                $(pvt.settings.flasher).each(function() {
                this.flash();
                });
            }
        }

        pvt.build_keyguide = function(iters) {
            if (!pvt.settings.guide) { return; }
            var keyguide = $(pvt.settings.guide).children("ol").first();
            keyguide.empty();
            var width_percent = 100/iters;
            var width_css = width_percent.toFixed(2)+"%";
            for (var i = 0; i < iters; i++) {
                var tk = pvt.target_key(i);
                keyguide.append('<li><code>'+tk+'</code></li>');
            }
            keyguide.find('li').css('width', width_css);
        }
        
        pvt.start = function() {
            pvt.send_log("start");
            pvt.change_state('running');
            pvt.show_status('running');
        };
        
        pvt.finish = function() {
            pvt.send_log("finish");
            // Ensure our average time is OK...
            if (pvt.fails_timing(pvt.times)) {
                pvt.throw_error('err_timing');
                return;
            }
            pvt.change_state('finished');
            pvt.show_status('success');
        }
        
        pvt.throw_error = function(err_name) {
            pvt.send_log(err_name);
            pvt.change_state('error');
            pvt.show_status(err_name);
        }
        
        pvt.show_status = function(name) {
            $(pvt.settings.status_container).children().hide();
            $('#'+name).show();
            if (pvt.settings.guide) {
                if (name === 'getready' || name === 'running') {
                    $(pvt.settings.guide).show();
                }
            }
        }
        
        pvt.change_state = function(new_state) {
            pvt.run_state = new_state;
        }
        
        pvt.target_key = function(idx) {
            var cycle_pos = ((idx+1) % pvt.settings.cycle_length);
            if (cycle_pos === 0) {
                return pvt.settings.reset_key;
            } else {
                return pvt.settings.count_key;
            }
        }
        
        pvt.highlight_guide = function() {
            if (!pvt.settings.guide) { return ;}
            var idx = pvt.presses.length - 1;
            var items = $(pvt.settings.guide).find('li');
            items.removeClass('current');
            items.slice(idx, idx+1).addClass('current');
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
            var tk = pvt.target_key(pvt.presses.length);
            var ck = pvt.settings.count_key;
            var rk = pvt.settings.reset_key;
            
            pvt.flash()
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

            pvt.highlight_guide();
            
            // Finally, if we've got enough, we have success!
            if (pvt.presses.length >= pvt.iters) {
                pvt.finish();
            }
            // And we can just fall through. Overall timing errors will be
            // caught in finish()
        }
        
        $(document).keydown(function(evt) {
            var keyChar = String.fromCharCode(evt.keyCode);
            if (pvt.currently_pressed[keyChar]) {
                // Don't re-handle an already pressed key
                return;
            }
            pvt.currently_pressed[keyChar] = {'keydown': evt}
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
        
        $(document).keyup(function(evt) {
            // Don't need as much logic here as in the run() version --
            // we'll just delete from our list regardless.
            var keyChar = String.fromCharCode(evt.keyCode);
            delete pvt.currently_pressed[keyChar];
        });
        pvt.reset();
    }
})(jQuery);

/*
    http://www.JSON.org/json2.js
    2011-01-18

    Public Domain.

    NO WARRANTY EXPRESSED OR IMPLIED. USE AT YOUR OWN RISK.

    See http://www.JSON.org/js.html


    This code should be minified before deployment.
    See http://javascript.crockford.com/jsmin.html

    USE YOUR OWN COPY. IT IS EXTREMELY UNWISE TO LOAD CODE FROM SERVERS YOU DO
    NOT CONTROL.


    This file creates a global JSON object containing two methods: stringify
    and parse.

        JSON.stringify(value, replacer, space)
            value       any JavaScript value, usually an object or array.

            replacer    an optional parameter that determines how object
                        values are stringified for objects. It can be a
                        function or an array of strings.

            space       an optional parameter that specifies the indentation
                        of nested structures. If it is omitted, the text will
                        be packed without extra whitespace. If it is a number,
                        it will specify the number of spaces to indent at each
                        level. If it is a string (such as '\t' or '&nbsp;'),
                        it contains the characters used to indent at each level.

            This method produces a JSON text from a JavaScript value.

            When an object value is found, if the object contains a toJSON
            method, its toJSON method will be called and the result will be
            stringified. A toJSON method does not serialize: it returns the
            value represented by the name/value pair that should be serialized,
            or undefined if nothing should be serialized. The toJSON method
            will be passed the key associated with the value, and this will be
            bound to the value

            For example, this would serialize Dates as ISO strings.

                Date.prototype.toJSON = function (key) {
                    function f(n) {
                        // Format integers to have at least two digits.
                        return n < 10 ? '0' + n : n;
                    }

                    return this.getUTCFullYear()   + '-' +
                         f(this.getUTCMonth() + 1) + '-' +
                         f(this.getUTCDate())      + 'T' +
                         f(this.getUTCHours())     + ':' +
                         f(this.getUTCMinutes())   + ':' +
                         f(this.getUTCSeconds())   + 'Z';
                };

            You can provide an optional replacer method. It will be passed the
            key and value of each member, with this bound to the containing
            object. The value that is returned from your method will be
            serialized. If your method returns undefined, then the member will
            be excluded from the serialization.

            If the replacer parameter is an array of strings, then it will be
            used to select the members to be serialized. It filters the results
            such that only members with keys listed in the replacer array are
            stringified.

            Values that do not have JSON representations, such as undefined or
            functions, will not be serialized. Such values in objects will be
            dropped; in arrays they will be replaced with null. You can use
            a replacer function to replace those with JSON values.
            JSON.stringify(undefined) returns undefined.

            The optional space parameter produces a stringification of the
            value that is filled with line breaks and indentation to make it
            easier to read.

            If the space parameter is a non-empty string, then that string will
            be used for indentation. If the space parameter is a number, then
            the indentation will be that many spaces.

            Example:

            text = JSON.stringify(['e', {pluribus: 'unum'}]);
            // text is '["e",{"pluribus":"unum"}]'


            text = JSON.stringify(['e', {pluribus: 'unum'}], null, '\t');
            // text is '[\n\t"e",\n\t{\n\t\t"pluribus": "unum"\n\t}\n]'

            text = JSON.stringify([new Date()], function (key, value) {
                return this[key] instanceof Date ?
                    'Date(' + this[key] + ')' : value;
            });
            // text is '["Date(---current time---)"]'


        JSON.parse(text, reviver)
            This method parses a JSON text to produce an object or array.
            It can throw a SyntaxError exception.

            The optional reviver parameter is a function that can filter and
            transform the results. It receives each of the keys and values,
            and its return value is used instead of the original value.
            If it returns what it received, then the structure is not modified.
            If it returns undefined then the member is deleted.

            Example:

            // Parse the text. Values that look like ISO date strings will
            // be converted to Date objects.

            myData = JSON.parse(text, function (key, value) {
                var a;
                if (typeof value === 'string') {
                    a =
/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2}(?:\.\d*)?)Z$/.exec(value);
                    if (a) {
                        return new Date(Date.UTC(+a[1], +a[2] - 1, +a[3], +a[4],
                            +a[5], +a[6]));
                    }
                }
                return value;
            });

            myData = JSON.parse('["Date(09/09/2001)"]', function (key, value) {
                var d;
                if (typeof value === 'string' &&
                        value.slice(0, 5) === 'Date(' &&
                        value.slice(-1) === ')') {
                    d = new Date(value.slice(5, -1));
                    if (d) {
                        return d;
                    }
                }
                return value;
            });


    This is a reference implementation. You are free to copy, modify, or
    redistribute.
*/

/*jslint evil: true, strict: false, regexp: false */

/*members "", "\b", "\t", "\n", "\f", "\r", "\"", JSON, "\\", apply,
    call, charCodeAt, getUTCDate, getUTCFullYear, getUTCHours,
    getUTCMinutes, getUTCMonth, getUTCSeconds, hasOwnProperty, join,
    lastIndex, length, parse, prototype, push, replace, slice, stringify,
    test, toJSON, toString, valueOf
*/


// Create a JSON object only if one does not already exist. We create the
// methods in a closure to avoid creating global variables.

var JSON;
if (!JSON) {
    JSON = {};
}

(function () {
    "use strict";

    function f(n) {
        // Format integers to have at least two digits.
        return n < 10 ? '0' + n : n;
    }

    if (typeof Date.prototype.toJSON !== 'function') {

        Date.prototype.toJSON = function (key) {

            return isFinite(this.valueOf()) ?
                this.getUTCFullYear()     + '-' +
                f(this.getUTCMonth() + 1) + '-' +
                f(this.getUTCDate())      + 'T' +
                f(this.getUTCHours())     + ':' +
                f(this.getUTCMinutes())   + ':' +
                f(this.getUTCSeconds())   + 'Z' : null;
        };

        String.prototype.toJSON      =
            Number.prototype.toJSON  =
            Boolean.prototype.toJSON = function (key) {
                return this.valueOf();
            };
    }

    var cx = /[\u0000\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g,
        escapable = /[\\\"\x00-\x1f\x7f-\x9f\u00ad\u0600-\u0604\u070f\u17b4\u17b5\u200c-\u200f\u2028-\u202f\u2060-\u206f\ufeff\ufff0-\uffff]/g,
        gap,
        indent,
        meta = {    // table of character substitutions
            '\b': '\\b',
            '\t': '\\t',
            '\n': '\\n',
            '\f': '\\f',
            '\r': '\\r',
            '"' : '\\"',
            '\\': '\\\\'
        },
        rep;


    function quote(string) {

// If the string contains no control characters, no quote characters, and no
// backslash characters, then we can safely slap some quotes around it.
// Otherwise we must also replace the offending characters with safe escape
// sequences.

        escapable.lastIndex = 0;
        return escapable.test(string) ? '"' + string.replace(escapable, function (a) {
            var c = meta[a];
            return typeof c === 'string' ? c :
                '\\u' + ('0000' + a.charCodeAt(0).toString(16)).slice(-4);
        }) + '"' : '"' + string + '"';
    }


    function str(key, holder) {

// Produce a string from holder[key].

        var i,          // The loop counter.
            k,          // The member key.
            v,          // The member value.
            length,
            mind = gap,
            partial,
            value = holder[key];

// If the value has a toJSON method, call it to obtain a replacement value.

        if (value && typeof value === 'object' &&
                typeof value.toJSON === 'function') {
            value = value.toJSON(key);
        }

// If we were called with a replacer function, then call the replacer to
// obtain a replacement value.

        if (typeof rep === 'function') {
            value = rep.call(holder, key, value);
        }

// What happens next depends on the value's type.

        switch (typeof value) {
        case 'string':
            return quote(value);

        case 'number':

// JSON numbers must be finite. Encode non-finite numbers as null.

            return isFinite(value) ? String(value) : 'null';

        case 'boolean':
        case 'null':

// If the value is a boolean or null, convert it to a string. Note:
// typeof null does not produce 'null'. The case is included here in
// the remote chance that this gets fixed someday.

            return String(value);

// If the type is 'object', we might be dealing with an object or an array or
// null.

        case 'object':

// Due to a specification blunder in ECMAScript, typeof null is 'object',
// so watch out for that case.

            if (!value) {
                return 'null';
            }

// Make an array to hold the partial results of stringifying this object value.

            gap += indent;
            partial = [];

// Is the value an array?

            if (Object.prototype.toString.apply(value) === '[object Array]') {

// The value is an array. Stringify every element. Use null as a placeholder
// for non-JSON values.

                length = value.length;
                for (i = 0; i < length; i += 1) {
                    partial[i] = str(i, value) || 'null';
                }

// Join all of the elements together, separated with commas, and wrap them in
// brackets.

                v = partial.length === 0 ? '[]' : gap ?
                    '[\n' + gap + partial.join(',\n' + gap) + '\n' + mind + ']' :
                    '[' + partial.join(',') + ']';
                gap = mind;
                return v;
            }

// If the replacer is an array, use it to select the members to be stringified.

            if (rep && typeof rep === 'object') {
                length = rep.length;
                for (i = 0; i < length; i += 1) {
                    k = rep[i];
                    if (typeof k === 'string') {
                        v = str(k, value);
                        if (v) {
                            partial.push(quote(k) + (gap ? ': ' : ':') + v);
                        }
                    }
                }
            } else {

// Otherwise, iterate through all of the keys in the object.

                for (k in value) {
                    if (Object.hasOwnProperty.call(value, k)) {
                        v = str(k, value);
                        if (v) {
                            partial.push(quote(k) + (gap ? ': ' : ':') + v);
                        }
                    }
                }
            }

// Join all of the member texts together, separated with commas,
// and wrap them in braces.

            v = partial.length === 0 ? '{}' : gap ?
                '{\n' + gap + partial.join(',\n' + gap) + '\n' + mind + '}' :
                '{' + partial.join(',') + '}';
            gap = mind;
            return v;
        }
    }

// If the JSON object does not yet have a stringify method, give it one.

    if (typeof JSON.stringify !== 'function') {
        JSON.stringify = function (value, replacer, space) {

// The stringify method takes a value and an optional replacer, and an optional
// space parameter, and returns a JSON text. The replacer can be a function
// that can replace values, or an array of strings that will select the keys.
// A default replacer method can be provided. Use of the space parameter can
// produce text that is more easily readable.

            var i;
            gap = '';
            indent = '';

// If the space parameter is a number, make an indent string containing that
// many spaces.

            if (typeof space === 'number') {
                for (i = 0; i < space; i += 1) {
                    indent += ' ';
                }

// If the space parameter is a string, it will be used as the indent string.

            } else if (typeof space === 'string') {
                indent = space;
            }

// If there is a replacer, it must be a function or an array.
// Otherwise, throw an error.

            rep = replacer;
            if (replacer && typeof replacer !== 'function' &&
                    (typeof replacer !== 'object' ||
                    typeof replacer.length !== 'number')) {
                throw new Error('JSON.stringify');
            }

// Make a fake root object containing our value under the key of ''.
// Return the result of stringifying the value.

            return str('', {'': value});
        };
    }


// If the JSON object does not yet have a parse method, give it one.

    if (typeof JSON.parse !== 'function') {
        JSON.parse = function (text, reviver) {

// The parse method takes a text and an optional reviver function, and returns
// a JavaScript value if the text is a valid JSON text.

            var j;

            function walk(holder, key) {

// The walk method is used to recursively walk the resulting structure so
// that modifications can be made.

                var k, v, value = holder[key];
                if (value && typeof value === 'object') {
                    for (k in value) {
                        if (Object.hasOwnProperty.call(value, k)) {
                            v = walk(value, k);
                            if (v !== undefined) {
                                value[k] = v;
                            } else {
                                delete value[k];
                            }
                        }
                    }
                }
                return reviver.call(holder, key, value);
            }


// Parsing happens in four stages. In the first stage, we replace certain
// Unicode characters with escape sequences. JavaScript handles many characters
// incorrectly, either silently deleting them, or treating them as line endings.

            text = String(text);
            cx.lastIndex = 0;
            if (cx.test(text)) {
                text = text.replace(cx, function (a) {
                    return '\\u' +
                        ('0000' + a.charCodeAt(0).toString(16)).slice(-4);
                });
            }

// In the second stage, we run the text against regular expressions that look
// for non-JSON patterns. We are especially concerned with '()' and 'new'
// because they can cause invocation, and '=' because it can cause mutation.
// But just to be safe, we want to reject all unexpected forms.

// We split the second stage into 4 regexp operations in order to work around
// crippling inefficiencies in IE's and Safari's regexp engines. First we
// replace the JSON backslash pairs with '@' (a non-JSON character). Second, we
// replace all simple value tokens with ']' characters. Third, we delete all
// open brackets that follow a colon or comma or that begin the text. Finally,
// we look to see that the remaining characters are only whitespace or ']' or
// ',' or ':' or '{' or '}'. If that is so, then the text is safe for eval.

            if (/^[\],:{}\s]*$/
                    .test(text.replace(/\\(?:["\\\/bfnrt]|u[0-9a-fA-F]{4})/g, '@')
                        .replace(/"[^"\\\n\r]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g, ']')
                        .replace(/(?:^|:|,)(?:\s*\[)+/g, ''))) {

// In the third stage we use the eval function to compile the text into a
// JavaScript structure. The '{' operator is subject to a syntactic ambiguity
// in JavaScript: it can begin a block or an object literal. We wrap the text
// in parens to eliminate the ambiguity.

                j = eval('(' + text + ')');

// In the optional fourth stage, we recursively walk the new structure, passing
// each name/value pair to a reviver function for possible transformation.

                return typeof reviver === 'function' ?
                    walk({'': j}, '') : j;
            }

// If the text is not JSON parseable, then a SyntaxError is thrown.

            throw new SyntaxError('JSON.parse');
        };
    }
}());