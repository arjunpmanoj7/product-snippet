odoo.define('point_of_sale.CreateSaleOrderPopup', function(require){
    'use strict';
///** @odoo-module */
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require("@web/core/utils/hooks");
    const { _lt } = require('@web/core/l10n/translation');
    var rpc =require('web.rpc')
    const ajax = require('web.ajax');
    const { useState, onMounted } = owl;
    var this_orderline;
    class CreatePreOrderPopup extends AbstractAwaitablePopup {
        setup() {
            super.setup();
            useListener('send_to_kitchen', this._onClickReOrderConfirm);
        }
        async _onClickReOrderConfirm(e)
        {
                  if (!this.clicked) {
                  try {
                    this.clicked = true;
                    console.log('this.pos.config.iface_printers',this.env.pos.config.iface_printers)
                    const order = this.env.pos.get_order();
//                    order.is_preorder = true
                    if (order.hasChangesToPrint()) {
                        const isPrintSuccessful = await order.printChanges();
                        console.log('isPrintSuccessful',isPrintSuccessful)
                        if (isPrintSuccessful) {
                            order.updatePrintedResume();
                        } else {
                            this.showPopup('ErrorPopup', {
                                title: this.env._t('Printing failed'),
                                body: this.env._t('Failed in printing the changes in the order'),
                            });
                        }
                    }
                } finally {
                    this.clicked = false;
                }
            }
            this.env.posbus.trigger('close-popup', {
                popupId: this.props.id
                });
        }
        get currentOrder() {
            return this.env.pos.get_order();
        }
        get addedClasses() {
            if (!this.currentOrder) return {};
            const hasChanges = this.currentOrder.hasChangesToPrint();
            const skipped = hasChanges ? false : this.currentOrder.hasSkippedChanges();
            return {
                highlight: hasChanges,
                altlight: skipped,
            };
        }
    }
    CreatePreOrderPopup.template = 'CreatePreOrderPopup';
    CreatePreOrderPopup.defaultProps = {
        confirmText: _lt('Confirm'),
        cancelText: _lt('Cancel'),
        title: _lt('Confirm ?'),
        body: '',
    };

    Registries.Component.add(CreateSaleOrderPopup);

    return CreateSaleOrderPopup;
});