# Flow Built-In Type Completion

This is a sublime plugin for flow built-in type auto completion.

## Install

The easiest way to install this is with [Package Control](https://sublime.wbond.net/).

 * Bring up the Command Palette (Command+Shift+p on OS X, Control+Shift+p on Linux/Windows).
 * Select "Package Control: Install Package" (it'll take a few seconds)
 * Select **Flow Built-In Type Completion** when the list appears.

Package Control will automatically keep the package up to date with the latest version.

## Built-In Types in Flow 0.12.0

#### [BOM Built-In Types](https://github.com/facebook/flow/blob/v0.12.0/lib/bom.js)

```
History, Location, DOMParser, FormData, MutationRecord, MutationObserver, 
WebSocket, Worker, XDomainRequest, XMLHttpRequest, XMLHttpRequestEventTarget, 
XMLSerializer, Geolocation, Position, Coordinates, PositionError, 
PositionOptions
```

#### [CORE Built-In Types](https://github.com/facebook/flow/blob/v0.12.0/lib/core.js)

```
Object, Symbol, Function, Boolean, Number, Array, String, RegExp, Date, Error, 
EvalError, RangeError, ReferenceError, SyntaxError, TypeError, URIError, JSON, 
Map, WeakMap, Set, Promise, ArrayBuffer, ArrayBufferView, Int8Array, 
Uint8Array, Uint8ClampedArray, Int16Array, Uint16Array, Int32Array, 
Uint32Array, Float32Array, Float64Array, DataView
```

#### PRIMITIVE Built-In Types

```
boolean, string, void, any, mixed, number
```

#### [CSSOM Built-In Types](https://github.com/facebook/flow/blob/v0.12.0/lib/cssom.js)

```
StyleSheet, CSSStyleSheet, CSSRule, CSSRuleList, CSSStyleDeclaration
```

#### [DOM Built-In Types](https://github.com/facebook/flow/blob/v0.12.0/lib/dom.js)

```
Blob, FileReader, BaseReader, File, FileList, DOMError, EventTarget, Event, 
ProgressEvent, MessageEvent, Node, NodeList, NamedNodeMap, Attr, 
HTMLCollection, Document, DocumentFragment, Range, DOMTokenList, Element, 
HTMLElement, HTMLBaseElement, CanvasGradient, CanvasPattern, ImageBitmap, 
HitRegionOptions, CanvasDrawingStyles, SVGMatrix, TextMetrics, Path2D, 
ImageData, CanvasRenderingContext2D, WebGLRenderingContext, HTMLCanvasElement,
 HTMLCollection, HTMLFormElement, HTMLImageElement, Image, MediaError, 
 TimeRanges, AudioTrack, AudioTrackList, VideoTrack, VideoTrackList, 
 TextTrackCue, TextTrackCueList, TextTrack, TextTrackList, HTMLMediaElement, 
 HTMLVideoElement, HTMLInputElement, HTMLButtonElement, HTMLTextAreaElement, 
 HTMLSelectElement, HTMLOptionsCollection, HTMLAnchorElement, 
 HTMLScriptElement, HTMLStyleElement, TextRange, ClientRect, ClientRectList, 
 DOMImplementation, DocumentType, CharacterData, Text, Comment, URL, 
 MediaSource, SourceBuffer, SourceBufferList, Storage, TrackDefaultList, 
 TrackDefault
```

#### [NODE Built-In Types](https://github.com/facebook/flow/blob/v0.12.0/lib/node.js)

```
Buffer
```

#### [REACT Built-In Types](https://github.com/facebook/flow/blob/v0.12.0/lib/react.js)

```
ReactComponent, ReactElement, SyntheticEvent, SyntheticClipboardEvent, 
SyntheticCompositionEvent, SyntheticInputEvent, SyntheticUIEvent, 
SyntheticFocusEvent, SyntheticKeyboardEvent, SyntheticMouseEvent, 
SyntheticDragEvent, SyntheticWheelEvent, SyntheticTouchEvent
```


## Issues & Feature Requests

Please use [GitHub Issue Tracker](https://github.com/xinchaobeta/flow-builtin-type-completion/issues) to report any bugs and make feature requests.

## Licensing
Licensed under permissive MIT-style license
