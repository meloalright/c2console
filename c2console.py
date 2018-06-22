'''
 c2console v1.2.0
 @meloalright
'''
import sublime
import sublime_plugin
import re
import os

def plugin_loaded():
    print('c2console loaded')

class c2console(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):

        snippet = []
        is_inside_tag = view.match_selector(locations[0],
                "source.js")
        # if not js scope then return
        if not is_inside_tag:
            return snippet
        # only works on specific input
        match = re.compile(prefix).match('console')

        if match:
            #automatic fill here
            snippet = [
                ['console.log();', ('console.log(${1});')],
                ['console.info();', ('console.info(${1});')],
                ['console.table();', ('console.table(${1});')],
                ['console.error();', ('console.error(${1});')],
                ['console.debug();', ('console.debug(${1});')],
                ['console.warn();', ('console.warn(${1});')],
                ['console.dir();', ('console.dir(${1});')],
                ['console.dirxml();', ('console.dirxml(${1});')],
                ['console.trace();', ('console.trace(${1});')],
                ['console.group();', ('console.group(${1});')],
                ['console.groupCollapsed();', ('console.groupCollapsed(${1});')],
                ['console.groupEnd();', ('console.groupEnd(${1});')],
                ['console.clear();', ('console.clear(${1});')],
                ['console.count();', ('console.count(${1});')],
                ['console.assert();', ('console.assert(${1});')],
                ['console.markTimeline();', ('console.markTimeline(${1});')],
                ['console.profile();', ('console.profile(${1});')],
                ['console.profileEnd();', ('console.profileEnd(${1});')],
                ['console.timeline();', ('console.timeline(${1});')],
                ['console.timelineEnd();', ('console.timelineEnd(${1});')],
                ['console.time();', ('console.time(${1});')],
                ['console.timeEnd();', ('console.timeEnd(${1});')],
                ['console.timeStamp();', ('console.timeStamp(${1});')],
                ['console.context();', ('console.context(${1});')],
                ['console.memory();', ('console.memory(${1});')]
            ]

        return snippet
