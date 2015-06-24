import sys, os, sublime, sublime_plugin

if sys.version_info < (3, 0):
    from completions import types
else:
    from .completions import types

def isJSX(view=None):
  if view is None:
      view = sublime.active_window().active_view()
  scope_name_arr = view.scope_name(0).split()
  return 'source.js' in scope_name_arr

class FlowBuiltinTypeCompletion(sublime_plugin.EventListener):

  def on_query_completions(self, view, prefix, locations):
    if isJSX(view):
      trigger_start = locations[0] - len(prefix)
      line = sublime.Region(view.line(trigger_start).begin(), trigger_start)
      if view.substr(line).strip().endswith(':'):
        return types

