from .completions import primitive, bom, core, cssom, dom, node, react
import sublime, sublime_plugin

completions_type = primitive.types + bom.types + core.types + cssom.types + dom.types + node.types + react.types

def isJSX(view=None):
  if view is None:
      view = sublime.active_window().active_view()
  scope_name_arr = view.scope_name(0).split()
  return 'source.js' in scope_name_arr or 'source.js.jsx' in scope_name_arr

class FlowBuiltinTypeCompletion(sublime_plugin.EventListener):

  def on_query_completions(self, view, prefix, locations):
    if isJSX(view):
      trigger_start = locations[0] - len(prefix)
      line = sublime.Region(view.line(trigger_start).begin(), trigger_start)
      if view.substr(line).strip().endswith(':'):
        return completions_type

