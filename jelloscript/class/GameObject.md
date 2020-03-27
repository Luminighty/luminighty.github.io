
# GameObject
The super class for every GameObject

## Properties
| Name | Description | Type |
| --- | --- | --- |
| position | The position of the object  | [Vector2] |
| size | The size of the object, this is used for collision and rendering by default  | [Vector2] |
| enabled | If set to false the object won't call Update() and won't be shown in the game | [Boolean]
| hidden | If set to true the object won't be rendered, however it'll still call the Update() method | [Boolean]
| sprite | The sprite to be rendered | [Sprite]
| spriteRect | Stores the sprite's rect, should be updated when sprite is called | [Rect]
| spriteFlipX | True if the sprite should be flipped on the X axis | [Boolean]
| spriteFlipY | True if the sprite should be flipped on the Y axis | [Boolean]
## Methods
| Name | Description | Returns |
| --- | --- | --- |
| update(tick) | Called every tick | |
| onEnabled() | Called whenever the object was active and got disabled. Note it isn't called on initialization. Use the constructor for that |
| onDisabled() | Called whenever the object was deactive and got activated |
| onHidden() | Called whenever the object was shown and got hidden |
| onShown() | Called whenever the object was hidden and got shown |
| onDestroy() | Called whenever the object was destroyed |
| GameObject.init(GameObject) | Initializes a gameobject and adds it to the gameObjects list |

## Usage Example:
```javascript
import GameObject from './engine/GameObject';
import {sprites} from './engine/Sprite';
import * as Input from './engine/input';

// It isn't necessary to export it, however it's very likely that you'll have to access it at one point in a different file
export default class Player extends GameObject {
	constructor() {
		super(); // the super constructor should always be called
		this.position = {x: 10, y: 10};
		this.sprite = sprites.player;
	}

	// Called every tick
	update(tick) {
		this.position.x += Input.Axes.Horizontal.value;
		this.position.y += Input.Axes.Vertical.value;
	}

	onEnabled() {
		console.log("Player enabled");
	}
}

// initializing a player object
GameObject.init(new Player());
```

<sub>See also [Sprite], [Vector2], [Rect],  [Boolean]</sub>

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