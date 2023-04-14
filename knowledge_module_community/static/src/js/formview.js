/** @odoo-module */

import { formView } from '@web/views/form/form_view';
import { FormCompiler } from '@web/views/form/form_compiler';
import { registry } from "@web/core/registry";
import { createElement } from "@web/core/utils/xml";
import { ComKnowledgeFormRender } from '@knowledge_module_community/js/myknowledgeformrender';
export const MyKnowledgeArticleView = {
    ...formView,
    Renderer: ComKnowledgeFormRender,
};

registry.category("views").add("my_knowledge_article_form", MyKnowledgeArticleView);