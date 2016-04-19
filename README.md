# Flow Built-In Type Completion

This is a sublime plugin for [flow](https://github.com/facebook/flow) built-in type auto completion.

## Install

The easiest way to install this is with [Package Control](https://sublime.wbond.net/).

 * Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Select **Flow Built-In Type Completion** when the list appears.

Package Control will automatically keep the package up to date with the latest version.

## Screenshots
![sample](https://raw.githubusercontent.com/xinchaobeta/flow-builtin-type-completion/master/screenshots/sample.png)


## Built-In Types in Flow [v0.23.0](https://github.com/facebook/flow/releases/tag/v0.23.0)

- [BOM Built-In Types](https://github.com/facebook/flow/blob/v0.23.0/lib/bom.js)

```
Screen, Navigator, MimeType, MimeTypeArray, Plugin, PluginArray, History, 
Location, DOMParser, FormData, MutationRecord, MutationObserver, 
CloseEvent, WebSocket, Worker, XDomainRequest, XMLHttpRequest, 
XMLHttpRequestEventTarget, XMLSerializer, Geolocation, Position, 
Coordinates, PositionError, AudioContext, AudioNode, AudioParam, 
AudioDestinationNode, AudioListener, AudioBuffer, AudioBufferSourceNode, 
MediaStream, MediaStreamTrack, MediaElementAudioSourceNode, 
MediaStreamAudioSourceNode, ScriptProcessorNode, AnalyserNode, 
BiquadFilterNode, ChannelMergerNode, ChannelSplitterNode, 
ConvolverNode, DelayNode, DynamicsCompressorNode, GainNode, 
OscillatorNode, PannerNode, PeriodicWave, WaveShaperNode, Headers, 
URLSearchParams, Response, Request
```

- [CORE Built-In Types](https://github.com/facebook/flow/blob/v0.23.0/lib/core.js)

```
Object, Symbol, Function, Boolean, Number, Array, 
String, RegExp, Date, Error, EvalError, RangeError, 
ReferenceError, SyntaxError, TypeError, URIError, 
JSON, Map, WeakMap, Set, WeakSet, Promise, ArrayBuffer, 
$TypedArray, Int8Array, Uint8Array, Uint8ClampedArray, 
Int16Array, Uint16Array, Int32Array, Uint32Array, 
Float32Array, Float64Array, DataView, Reflect
```

- PRIMITIVE Built-In Types

```
boolean, string, void, any, mixed, number
```

- [CSSOM Built-In Types](https://github.com/facebook/flow/blob/v0.23.0/lib/cssom.js)

```
StyleSheet, StyleSheetList, MediaList, CSSStyleSheet, 
CSSRule, CSSRuleList, CSSStyleDeclaration, TransitionEvent 
```

- [DOM Built-In Types](https://github.com/facebook/flow/blob/v0.23.0/lib/dom.js)

```
Blob, FileReader, BaseReader, File, FileList, DataTransfer, 
DataTransferItemList, DataTransferItem, DOMError, EventTarget, 
Event, UIEvent, MouseEvent, WheelEvent, DragEvent, 
ProgressEvent, MessageEvent, KeyboardEvent, Node, NodeList, 
NamedNodeMap, Attr, HTMLCollection, Document, DocumentFragment, 
Selection, Range, DOMTokenList, Element, HTMLElement, 
HTMLBaseElement, CanvasGradient, CanvasPattern, ImageBitmap, 
HitRegionOptions, CanvasDrawingStyles, SVGMatrix, TextMetrics, 
Path2D, ImageData, CanvasRenderingContext2D, 
WebGLRenderingContext, HTMLCanvasElement, HTMLFormElement, 
HTMLIFrameElement, HTMLImageElement, Image, MediaError, 
TimeRanges, AudioTrack, AudioTrackList, VideoTrack, 
VideoTrackList, TextTrackCue, TextTrackCueList, TextTrack, 
TextTrackList, HTMLMediaElement, HTMLVideoElement, 
HTMLInputElement, HTMLButtonElement, HTMLTextAreaElement, 
HTMLSelectElement, HTMLOptionsCollection, HTMLOptionElement, 
HTMLAnchorElement, HTMLLabelElement, HTMLLinkElement, 
HTMLScriptElement, HTMLStyleElement, HTMLParagraphElement, 
HTMLDivElement, HTMLSpanElement, HTMLAppletElement, 
HTMLEmbedElement, TextRange, ClientRect, ClientRectList, 
DOMImplementation, DocumentType, CharacterData, Text, 
Comment, URL, MediaSource, SourceBuffer, SourceBufferList, 
Storage, TrackDefaultList, TrackDefault, NodeFilter, 
NodeIterator, TreeWalker
```

- [NODE Built-In Types](https://github.com/facebook/flow/blob/v0.23.0/lib/node.js)

```
Buffer, Process
```

- [REACT Built-In Types](https://github.com/facebook/flow/blob/v0.23.0/lib/react.js)

```
React, LegacyReactComponent, React, SyntheticEvent, 
SyntheticClipboardEvent, SyntheticCompositionEvent, 
SyntheticInputEvent, SyntheticUIEvent, SyntheticFocusEvent, 
SyntheticKeyboardEvent, SyntheticMouseEvent, 
SyntheticDragEvent, SyntheticWheelEvent, SyntheticTouchEvent
```


## Issues & Feature Requests

Please use [GitHub Issue Tracker](https://github.com/xinchaobeta/flow-builtin-type-completion/issues) to report any bugs and make feature requests.

## Licensing
Licensed under permissive MIT-style license
