/** @odoo-module **/

import { FormRenderer } from "@web/views/form/form_renderer";
var rpc = require('web.rpc');
const Dialog = require('web.Dialog');
export class ComKnowledgeFormRender extends FormRenderer {
    setup() {
        console.log('check this');
        super.setup();
    }
    _MoreOptions(){

    }
    _FeedBack(){
        rpc.query({
                model: 'my.knowledge.article',
                method: 'chatter_knowledge',
                args: [this.env.model.__bm_load_params__.res_id]
            }).then(result => {
              console.log('result',result)
              if(result){
              this.state.chatter = result
              }
              else{
                this.state.chatter = result
              }
        });
    }

}
