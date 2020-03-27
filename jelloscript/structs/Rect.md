# Rect

Used to define a rectangle
 - x : Number
 - y : Number
 - w : Number (Width)
 - h : Number (Height)
```javascript
let rect = {x: 3, y: 5, w: 8, h: 8}; 
```
For easier usage and additional methods the Rect class exists inside the `Struct.js` module

```javascript
import {Rect} from './engine/Struct';

// the default constructor
let rect1 = new Rect(3, 5, 10, 12);
// It is possible to use an array for the constructor
let rect2 = new Rect([3, 5, 10, 12]);
// You can convert the other to a class
let rect3 = new Rect({x: 3, y: 5, w:10, h:12});
```

## Properties
| Name | Description | Type |
| --- | --- | --- |
| x | The x value for the top left position | [Number] |
| y | The y value for the top left position | [Number] |
| w | The width of the rect | [Number] |
| position | Returns the (x,y) value as a Vector2 | [Vector2] |
| size | Returns the (w,h) value as a Vector2 | [Vector2] |
| minX | The smaller value on the X axis | [Number] |
| minY | The smaller value on the Y axis | [Number] |
| maxX | The larger value on the X axis | [Number] |
| maxY | The larger value on the Y axis | [Number] |
| topLeft | Top Left position in Vector2 | [Vector2] |
| topRight | Top Right position in Vector2 | [Vector2] |
| bottomLeft | Bottom Left position in Vector2 | [Vector2] |
| bottomRight | Bottom Right position in Vector2 | [Vector2] |
| center | The center of the rect in Vector2 | [Vector2] |
|  |  |  |

## Methods
| Name | Description | Returns |
| --- | --- | --- |
| multiply | Multiplies the rect with the number using type | Rect |
| contains | Returns true if the rect contains the 'other' rect | [Boolean] |
| intersects | Returns true if the rect intersects the 'other' rect | [Boolean] |


## Static methods
| Name | Description | Returns |
| --- | --- | --- |
| initFromPositions | Creates a rect with 2 position | Rect |
| zero | Shorthand for new Rect(0,0,0,0) | Rect |

<sub>See also [Number], [Boolean], [Vector2]</sub>

[Back to Sections]

<!-- Files -->
[Quick Start]: Tutorial
[Inputs]: Input

<!-- Classes -->
[GameObject]: class/GameObject
[Component]: class/Component
[Animator]: class/Animator
[Sprite]: class/Sprite
[Sound]: class/Sound
[Resource]: class/Resource

<!-- Structs -->
[Structs]: structs/Structs
[Vector2]: structs/Vector2
[Rect]: structs/Rect
[Sprite Labels]: structs/SpriteLabel

<!-- Misc -->
[Back to Sections]: Home

<!-- External Links -->
[Boolean]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean
[Number]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number
[String]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String

[Element]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement
[AudioElement]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLAudioElement
[Image]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement
[Promise]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

[KeyboardEvent.code]: https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/code
[GamepadButton]: https://developer.mozilla.org/en-US/docs/Web/API/Gamepad/axes