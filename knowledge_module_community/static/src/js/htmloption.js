/** @odoo-module **/
import { ComponentWrapper } from 'web.OwlCompatibility';
import Wysiwyg from 'web_editor.wysiwyg';
import { qweb as QWeb, _t } from 'web.core';
import { preserveCursor } from '@web_editor/js/editor/odoo-editor/src/OdooEditor';

Wysiwyg.include({
    init: function (parent, options) {
        this._super.apply(this, arguments);
    },
    _getPowerboxOptions: function () {
        const options = this._super();

        const { commands, categories } = options;
        const knowledgeCategory = { name: _t('MyKnowledge'), priority: 40 };
        const itemVideoCommand = {
            category: _t('MyKnowledge'),
            name: _t('link video'),
            priority: 40,
            description: _t('Insert a video link'),
            fontawesome: 'fa-youtube-play',
            callback: () => {
                    this.openMediaDialog({noVideos: false, noImages: true, noIcons: true, noDocuments: true});
                },
        };
        const itemSectionCommand = {
            category: _t('MyKnowledge'),
            name: _t('Section Template'),
            priority: 40,
            description: _t('Insert a Template'),
            fontawesome: 'fa-clipboard',
            callback: this._onTemplateClicked.bind(this)

        };
        categories.push(knowledgeCategory);
        commands.push(itemVideoCommand);
        commands.push(itemSectionCommand);
        return {
            ...options,
            categories,
            commands
        };
    },

    _onTemplateClicked: function () {
    const section = '<section style="border: 2px dashed #999; padding: 10px; margin: 10px 0;"><h2 style="font-size: 24px; font-weight: bold;">Section Title</h2><p style="font-size: 16px; line-height: 1.5;">Section content goes here</p></section>';
    const selection = window.getSelection();
    const range = selection.getRangeAt(0);
    const node = range.createContextualFragment(section);
    range.insertNode(node);
},

});
