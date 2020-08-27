window.addEventListener("load", function() {
    (function($){
        $('#id_date_range').on('change', function (e) {
            var optionSelected = $("option:selected", this);
            var valueSelected = this.value;

            if (valueSelected === "Custom"){
                $('#id_start_date').hide();
                $("label[for=id_start_date").hide();
                $('.datetimeshortcuts').hide();
                $('.timezonewarning').hide();

                $('#id_end_date').hide();
                $("label[for=id_end_date").hide();
                $('.datetimeshortcuts').hide();
                $('.timezonewarning').hide();
            } else {
                $('#id_start_date').show();
                $("label[for=id_start_date").show();
                $('.datetimeshortcuts').show();
                $('.timezonewarning').show();

                $('#id_end_date').show();
                $("label[for=id_end_date").show();
                $('.datetimeshortcuts').show();
                $('.timezonewarning').show();
            }
        });
    })(django.jQuery);
});
