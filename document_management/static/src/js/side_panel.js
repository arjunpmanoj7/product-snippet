odoo.define('document.sidepanel', function(require) {
 "use strict";
 var core = require('web.core');
   var Dialog = require('web.Dialog');
   var _t = core._t;
   var KanbanController = require('web.KanbanController');
   var KanbanView = require('web.KanbanView');
   var viewRegistry = require('web.view_registry');
   var DocumentSearchPanel = require('document.search_panel');
   var QWeb = core.qweb;
   var ajax = require('web.ajax');
   var rpc = require('web.rpc');

   var KanbanButton = KanbanController.extend({
   start: function(){
   dragElement(document.getElementById("mydiv"));
        return this._super().then(function() {})
   },
    dragElement: function(elmnt) {
          var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
          if (document.getElementById(elmnt.id + "header")) {
            // if present, the header is where you move the DIV from:
            document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
          } else {
            // otherwise, move the DIV from anywhere inside the DIV:
            elmnt.onmousedown = dragMouseDown;
          }

          function dragMouseDown(e) {
            e = e || window.event;
            e.preventDefault();
            // get the mouse cursor position at startup:
            pos3 = e.clientX;
            pos4 = e.clientY;
            document.onmouseup = closeDragElement;
            // call a function whenever the cursor moves:
            document.onmousemove = elementDrag;
          }

          function elementDrag(e) {
            e = e || window.event;
            e.preventDefault();
            // calculate the new cursor position:
            pos1 = pos3 - e.clientX;
            pos2 = pos4 - e.clientY;
            pos3 = e.clientX;
            pos4 = e.clientY;
            // set the element's new position:
            elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
            elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
          }

          function closeDragElement() {
            // stop moving when mouse button is released:
            document.onmouseup = null;
            document.onmousemove = null;
          }
        }
   });
});