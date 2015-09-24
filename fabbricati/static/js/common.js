//GET COOKIE TO PROTECT SITE FROM CSRF attacks
//reference: https://docs.djangoproject.com/en/dev/ref/csrf/
//how to implement http://stackoverflow.com/questions/6506897/csrf-token-missing-or-incorrect-while-post-parameter-via-ajax-in-django

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }



$("tr.riga").click(function(){
    window.open("fabbricato/"+$(this).attr('id'),"_self");
});