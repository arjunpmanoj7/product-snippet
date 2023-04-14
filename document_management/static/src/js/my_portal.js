odoo.define("document.my_portal", function (require) {
    "use strict";
    var toast = $('.toast')
    $('.fa-share').on('click', function(){
        var self = this;
        var record_url = $(this).data('url')
        var $temp = $("<input>");
        $("body").append($temp);
        $temp.val(record_url).select();
        document.execCommand("copy");
        $temp.remove();
        toast.addClass('show');
        $('.toast-body').text(record_url)
    })
    $('.re-upload').on('click', function(){
        var self = this;
        var rec_id = $(this).data('id');
        var workspace_id = $(this).data('workspace_id');
        var workspace = $(this).data('workspace')
        var requested_by = $(this).data('requested_by')
        var requested_by = $(this).data('requested_by')
        $('#req_upload_form').modal('show');
        $('#workspace').val(workspace)
        $('#requested_by').val(requested_by)
        $('#workspace_id').val(workspace_id)
        $('#rec_id').val(rec_id)
    })
    $('.re-reject').on('click', function(){
        var self = this;
        var rec_id = $(this).data('id');
        $('#req_id').val(rec_id)
        $('#req_reject_form').modal('show');
        })
})


odoo.define('website_documents', function (require) {
    "use strict";
    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var ajax = require('web.ajax');


    $("#web_docs_upload").on('click', function () {
        $('#docs_upload_form').modal('show');
        console.log("choose workspace worked")
        rpc.query({
               model : 'document.workspace',
               method : 'work_spaces',
               args : []
        }).then(function(result){
           result.forEach(element =>{
             $('#workspace').append(`
             <option value="${element['id']}">${element['name']}</option>`
             )
           })
        })
    });

    $('#request').on('click', '.rec_upload', function () {
        console.log('it has click')
         $('#docs_upload_form').modal('show');
    })

})