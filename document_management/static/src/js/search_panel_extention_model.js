odoo.define("document.search_panel_extension", function (require) {
    "use strict";

    const ActionModel = require("web.ActionModel");
    const SearchPanelModelExtension = require("web.searchPanelModelExtension");

    const isFolderCategory = (s) => s.fieldName === "workspace_id";
    const isBoolean = (s) => s.fieldName === "boolean";

    class CustomDocumentSearchPanelModelExtension extends SearchPanelModelExtension {
        constructor() {
            super(...arguments);
            console.log("Searchpanel initialised....")
        }
        get(property) {

            switch (property) {

                case "selectedWorkspaceId": return this.getSections(isFolderCategory)[0]['activeValueId'];

            }
            return super.get(...arguments);
        }

        getFolders() {
            const { values } = this.getSections(isFolderCategory)[0];
            return [...values.values()];
        }

    }
    ActionModel.registry.add("CustomDocumentsSearchPanel", CustomDocumentSearchPanelModelExtension, 30);
    return CustomDocumentSearchPanelModelExtension;
    });