/** @odoo-module */

import { formView } from '@web/views/form/form_view';
import { registry } from "@web/core/registry";
import { ComSaleOrderRender } from '@js_class_blog/js/formrender';
console.log('SaleOrderRender',ComSaleOrderRender)
export const JsClassBlog = {
    ...formView,
    Renderer: ComSaleOrderRender,
};

registry.category("views").add("sale_order_blog", JsClassBlog);