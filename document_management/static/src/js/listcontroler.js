odoo.define('document.FormUploadButton', function(require) {
   "use strict";
    var viewRegistry = require('web.view_registry');
    var ListController = require('web.ListController');
    var ListView = require('web.ListView');
    var ListRenderer = require('web.ListRenderer');
    var DocumentSearchPanel = require('document.search_panel');
    var rpc = require('web.rpc');
    var Dialog = require('web.Dialog');
    var DocumentListView = ListView.extend({
       config: _.extend({}, ListView.prototype.config, {
           Controller: ListController,
           SearchPanel: DocumentSearchPanel,
       }),
   });
    viewRegistry.add('button_in_list_view', DocumentListView);
       Dialog.link = function (owner, message, options) {
    var buttons = [{
        text: _t("Ok"),
        close: true,
        click: options && options.confirm_callback,
    }];
    return new Dialog(owner, _.extend({
        size: 'medium',
        buttons: buttons,
        $content: $('<main/>', {
            role: 'alert',
            text: message,
        }),
        title: _t("Here's your Link !"),
        onForceClose: options && (options.onForceClose || options.confirm_callback),
    }, options)).open({shouldFocusButtons:true});
};
    ListController.include({
       buttons_template: 'UploadDocumentList.Buttons',
       events: _.extend({}, ListController.prototype.events, {
           'click .on_upload_doc_list': '_onUploadList',
       }),

    _onUploadList: function(){
        var self = this;
        var OnSelectedDocument = function(e){
            var SelectedFile = new FileReader();
            SelectedFile.onloadend= () =>{
            const base64String = SelectedFile.result;
            var workspace_id = self.searchModel.get('selectedWorkspaceId')
            console.log("SREE", workspace_id)
            rpc.query({
                    model: 'document.file',
                    method: 'document_file_create',
                    args: [base64String, this.files[0].name, workspace_id],
            }).then(function (result){
                console.log("RESULT", result)
                location.reload();
            });
            };
            let ll=['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']
if (this.files[0].type in ll){
    reader.readAsDataURL(this.files[0]);
}else{
   Dialog.link(this, "Upload xlsx files only");
}

            console.log("THIS", this)

        };
        var UploadFileDocument = $('<input type="file">');
        UploadFileDocument.click();
        UploadFileDocument.on('change', OnSelectedDocument);
    },
    });



return ListController
   });