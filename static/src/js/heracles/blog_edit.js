Module('blog_edit', function(){
    this.run = function(){
        $(function() {
            editor.init();
            ui.init();

            $('article[contenteditable="true"]').keydown(function(e) {
                if (e.keyCode === 13) {
                    document.execCommand( 'formatBlock', false, 'p' );
                }
            });
        });
    }
})

