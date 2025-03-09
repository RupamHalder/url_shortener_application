$(document).ready(function () {
    $(".btnCopyShortURL").click(function () {
        // Get the value from data attribute
        var textToCopy = $(this).data("short-url");

        // Create a temporary input element
        var tempInput = $("<input>");
        $("body").append(tempInput);
        tempInput.val(textToCopy).select();
        document.execCommand("copy");
        tempInput.remove();

        // Show copied message
        $("#url-copy-message").fadeIn().delay(1000).fadeOut();
    });
});