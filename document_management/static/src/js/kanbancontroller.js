odoo.define('document.uploadButton', function(require) {
   "use strict";
   var core = require('web.core');
   var Dialog = require('web.Dialog');
   var _t = core._t;
   var KanbanController = require('web.KanbanController');
   var KanbanView = require('web.KanbanView');
   var viewRegistry = require('web.view_registry');
   var DocumentSearchPanel = require('document.search_panel');
   var d=0;
   var rpc = require('web.rpc');
   var documents_selected = [];

   var KanbanButton = KanbanController.extend({
   buttons_template: 'button_in_kanban.button',
   events: _.extend({}, KanbanController.prototype.events, {
       'click .on_upload_doc': '_onUpload',
       'click .on_delete_button': '_onDelete',
       'click .on_share_button': '_onShare',
       'click .on_add_url': '_onAddUrl',
       'click .docs_check_box': '_onSelectDocs',
       'click .on_download_archive': '_onDownloadArchive',
       'click .on_download_local': '_onDownloadLocal',
       'click .on_archive_document': '_onArchiveDocument',
       'click .on_mail_document': '_onMailDocument',
       'click .on_copy_document': '_onCopyDocument',
       'click .on_create_task': '_onCreateTask',
       'click .on_create_lead': '_onCreateLead',
       'click .on_add_request': '_onRequestDoc',
   }),
   start: function(){
        return this._super().then(function() {})
   },
   _onMailDocument:function(ev){
       var self = this;
       rpc.query({
            model: 'document.file',
            method: 'on_mail_document',
            args: [documents_selected],
            }).then(function (result){
                self.do_action(result);
            });
       },
   _onCopyDocument:function(ev){
       var self=this;
       rpc.query({
            model: 'document.file',
            method: 'on_copy_document',
            args: [{
                'doc_id': documents_selected,
                }],
            }).then(function (result){
                self.do_action(result);
            });
   },
   _onRequestDoc:function(ev){
    var self = this;
    var workspace_id = this.searchModel.get('selectedWorkspaceId')
    rpc.query({
         model: 'request.document',
         method: 'action_request_doc',
         args: [workspace_id],
         }).then(function (result){
         self.do_action(result);
         })
    },
    _onArchiveDocument: function(ev){
        if (documents_selected.length != 0){
            rpc.query({
                model: 'document.file',
                method: 'document_file_archive',
                args: [documents_selected],
            }).then(function (result){
                documents_selected = []
                $('.docs_check_box').checked = false
                location.reload();
                });
            }
        else{
            Dialog.alert(this, "Please select least one document");
        }
   },
   _onSelectDocs: function(ev){
        var toast = $('.toast')
        var checked = $(ev.target).is(':checked');
        var record_id =parseInt($(ev.target).data('id'));
        if (checked){
            $('.o_legacy_kanban_view').css("max-width", "82%");
            toast.addClass('show');
            documents_selected.push(record_id);
        }
        else{
            let index = documents_selected.indexOf(record_id);
            documents_selected.splice(index, 1)
            if ( documents_selected.length == 0){
            $('.o_legacy_kanban_view').css("max-width", "100%");
            toast.removeClass('show');
            }
        }
   },

    _onDownloadLocal: function(){
     var a=documents_selected.pop();
        if (a>=1){
        this._ondownlaaaaaaa(a)
        }
        else{
        window.location.reload();
        }
    },

    _ondownlaaaaaaa: async function(element){
        var self = this
           await rpc.query({
                    model: 'document.file',
                    method: 'download_local',
                    args: [element]
                }).then(function(res){
                    var ss=res;
                    self.do_action(ss)
                    self._onDownloadLocal()
              })
       },

   _onDownloadArchive: function(ev){
        var self = this;
        if (documents_selected.length > 0) {
            rpc.query({
            model: 'document.file',
            method: 'archive_function',
            args: [documents_selected]
        }).then(function(res){
            self.do_action(res)
            })
        }
   },
   _onAddUrl: function(){
    var self = this;
    var workspace_id = this.searchModel.get('selectedWorkspaceId')
    $('.docs_check_box').checked = false;
    rpc.query({
            model: 'document.file',
            method: 'action_add_url',
            args: [workspace_id]
        }).then(function (result){
        documents_selected = []
            return self.do_action(result);
        });
   },
   _onCreateTask: function(){
    var self = this;
        rpc.query({
            model: 'document.file',
            method: 'action_btn_create_task',
            args: [documents_selected]
        }).then(function (result){
            if (result) {
                documents_selected = []
                location.reload();
            }
        });
   },
   _onCreateLead: function(){
    var self = this;
        rpc.query({
            model: 'document.file',
            method: 'action_btn_create_lead',
            args: [documents_selected]
        }).then(function (result){
            if (result) {
            documents_selected = []
                location.reload();
            }
        });
   },
   _onDelete: function(ev){
        var self = this;
        var record_id = parseInt($(ev.target).data('id'))
        rpc.query({
            model: 'document.file',
            method: 'document_file_delete',
            args: [documents_selected],
        }).then(function (result){
            documents_selected = []
            location.reload();
        });
   },
   _onShare: function(ev){
        var self = this;
        rpc.query({
            model: 'document.share',
            method: 'create_url',
            args: [documents_selected],
        }).then(function (result){
            self.do_action(result)
        });
   },

  _onUpload: function(){
        var workspace_id = this.searchModel.get('selectedWorkspaceId')
        this.do_action({
            name: "Upload Documents",
            type: 'ir.actions.act_window',
            res_model: 'document.file',
            view_mode: 'form',
            views: [[false, 'form']],
            target: 'new',
            context: {
            default_workspace_id: workspace_id,
            default_content_type: 'file',
        },
     })
  },
    updateButtons() {
        var Result='';
        var self=this;
        const selectedWorkspaceId = self.searchModel.get('selectedWorkspaceId');
        self.$buttons.find('.on_upload_doc').prop('disabled', !selectedWorkspaceId);
        self.$buttons.find('.on_add_url').prop('disabled', !selectedWorkspaceId);
        self.$buttons.find('.on_add_request').prop('disabled', !selectedWorkspaceId);


       },

    });


    var DocumentKanbanView = KanbanView.extend({
       config: _.extend({}, KanbanView.prototype.config, {
           Controller: KanbanButton,
           SearchPanel: DocumentSearchPanel,
       }),
   });
    viewRegistry.add('button_in_kanban_view', DocumentKanbanView);
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

});