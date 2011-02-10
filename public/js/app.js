$(function() {
   $('#instructions').instructions({'onfinish': function() {
       window.location.href = practice_path;
   }});
   
   
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

