let pb = $('#progress2')

function flash(message, category){
    var icon = 'icon-info-sign'
    if (category === 'error'){
        icon = 'icon-exclamation-sign'
        category='danger'
    } else if (category === 'success') {
       icon = 'icon-ok-sign'
    }
    let flash = $('<div style="margin-top:10px" class="alert alert-'+category+'"><i class="'+icon+'"></i>&nbsp;<a class="close" data-dismiss="alert">×</a>'+ message +'</div>')
    flash.insertAfter('#start-bg-job')
        // .hide().slideDown();
    // $.smoothScroll({
    //     scrollElement: $('body'),
    //     scrollTarget: '#mainContent'
    // });
}
function start_long_task() {
    // send ajax POST request to start background job
    pb.show()
    $.ajax({
        type: 'POST',
        url: '/longtask',
        success: function(data, status, request) {
            status_url = request.getResponseHeader('Location')
            update_progress(status_url)
        },
        error: function() {
            flash('Unexpected error', 'error')
        }
    });
}
function set_progress(pb, ps, percent, msg){
    pb.attr('aria-valuenow', '' + percent)
    pb.attr('style', 'width:' + percent + '%')
    pb.text(percent + '%')
    ps.text(msg)
}
function update_progress(status_url) {
    // send GET request to status URL
    let pb2 = $('#progress-bar2')
    let ps2 = $('#progress-status2')
    $.getJSON(status_url, function(data) {
        // update UI
        percent = parseInt(data['current'] * 100 / data['total']);
        set_progress(pb2, ps2, percent, data['status'])
        if (data['state'] !== 'PENDING' && data['state'] !== 'PROGRESS') {
            set_progress(pb2, ps2, 0, '')
            if ('result' in data) {
                // show result
                flash('Result: ' + data['result'], 'success')
            }
            else {
                // something unexpected happened
                flash('Result: ' + data['state'], 'warning')
            }
            pb.hide()
        }
        else {
            // rerun in 300 milli seconds
            setTimeout(function() {
                update_progress(status_url);
            }, 300);
        }
    });
}
$(function() {
    $('#start-bg-job').click(start_long_task);
});
