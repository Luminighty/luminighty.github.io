# Sprite Label

Used at sprite sheets for easier access
 - "LABEL1" : Vector2
 - "LABEL2" : Vector2
 - "LABEL3" : Vector2
 - ...

A sprite label is a dictionary of keys associated with a Vector2
The keys are required to be uppercase. (0,0) is the top-left sprite.


```javascript
let spriteLabel = {
	"WALK": {x:0, y:0},
	"RUN": {x:1, y:0},
	"IDLE": {x:3, y:1}
}; 
```
<sub>See [Sprites]</sub>

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