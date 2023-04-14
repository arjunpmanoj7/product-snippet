odoo.define("document.search_panel", function (require) {
    "use strict";
    const ActionModel = require("web.ActionModel");
    const searchPanel = require("web.searchPanel");

    class DocumentSearchPanel extends searchPanel {
        setup(){
            super.setup();
            console.log("tdugihftcgxd",this)
        }

    }
    DocumentSearchPanel.modelExtension = 'CustomDocumentsSearchPanel';
    return DocumentSearchPanel;
    });
