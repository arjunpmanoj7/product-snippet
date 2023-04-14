odoo.define('cw_pos.pos_order', function (require) {
"use strict";
var { PosGlobalState, Order} = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');

const PosSessionOrdersPosGlobalState = (PosGlobalState) => class PosSessionOrdersPosGlobalState extends PosGlobalState {
async _processData(loadedData) {
    await super._processData(...arguments);
    this.session_orders = loadedData['catch.weight'];
    console.log(this.session_orders,'llllllll')
    console.log(this.env.pos,'llllllwdsdsdssll')
    }
    }
Registries.Model.extend(PosGlobalState, PosSessionOrdersPosGlobalState);
});