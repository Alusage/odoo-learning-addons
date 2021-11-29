# -*- coding: utf-8 -*-

{
    "name": "Learning Event Partner",
    "version": "14.0.1.0.2",
    "depends": [
        #'__export__',
        "base",
        "event",
        "hr",
    ],
    "author": "Nicolas JEUDY, Odoo Community Association (OCA)",
    "installable": True,
    "data": [
        "views/event_menu_view.xml",
        "views/event_speakers_view.xml",
        "views/event_event_view.xml",
        "security/ir.model.access.csv",
    ],
}
