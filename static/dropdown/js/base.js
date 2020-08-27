window.addEventListener("load", function() {
    (function($){
        $('#id_date_range').on('change', function (e) {
            var optionSelected = $("option:selected", this);
            var valueSelected = this.value;

            if (valueSelected === "Custom"){
                $('.abcdefg').hide();
                $("label[for=id_start_date").hide();
            } else {
                $('.abcdefg').show();
                $("label[for=id_start_date").show();
            }
        });
    })(django.jQuery);
});
