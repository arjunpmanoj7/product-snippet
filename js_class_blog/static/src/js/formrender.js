/** @odoo-module **/
import { FormRenderer } from "@web/views/form/form_renderer";
const Dialog = require('web.Dialog');
export class ComSaleOrderRender extends FormRenderer {
    setup() {
        super.setup();
    }
    _MoreOptions(){
                    var dialog = new Dialog(null, {
                        title: "js class blog",
                        size: 'medium',
                        $content: $('<div/>', {
                            html: 'hai'
                        }),
                        buttons: [{
                            text: "Close",
                            close: true
                        }]
                    });
                    dialog.open();
    }
}
