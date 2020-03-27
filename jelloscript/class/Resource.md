# Resource
<sub>Implementing classes: [Sprite], [Sound]</sub>

Abstract base class for any DOM element resource. Other resource types should be inherited from this class.

## Properties
| Name | Description | Type |
| --- | --- | --- |
| element | The DOM element, if it's value is null when trying to acces it, it'll load it first | [Element] |
| path | The resource's physical file path | [String] |

## Methods
| Name | Description | Returns |
| --- | --- | --- |
| load | Creates a new [Element] and sets it as a reference to the `element` property |  |
| unload | Unloads the resource for memory management issues. |  |

<sub>See also [Sprite], [Sound], [Element], [String]</sub>

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