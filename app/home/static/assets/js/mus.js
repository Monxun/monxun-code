function load_delay(url='', duration=500)
{
    function delay () {
        setTimeout( function() { window.location = url }, duration );
    }
}