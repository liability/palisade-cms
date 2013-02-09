(function( $ ){

  $.fn.boxEditor = function( options ) {
    
    // Create some defaults, extending them with any options that were provided
    var settings = $.extend( {
      'location'         : 'top',
      'background-color' : '#ddd'
    }, options);

    return this.each(function() {

        var $this = $(this);

        $this.css("background-color",settings['background-color']);

        //$this.prepend("<div class='edit'>x</div>")

        $this.click(function () {
            console.log('clock '+$this.attr('id'));
        });
        
    });

  };
})( jQuery );