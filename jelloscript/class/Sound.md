# Sound
<sub>Extends [Resource]</sub>

Sounds are used to play sound effects or music for the player.

## Properties
| Name | Description | Type |
| --- | --- | --- |
| element | The DOM element, if it's value is null when trying to acces it, it'll load it first | [AudioElement] |
| path | The resource's physical file path | [String] |
| paused | Whenever the audio is paused or not | [Boolean] |
| volume | The volume of the sound in the interval [0, 1] | [Number] |
| muted | Whenever the audio is muted or not | [Boolean] |
| duration | The length of the sound (readonly) | [Number] |
| loop | Whenever the audio is looping or not | [Boolean] |
| currentTime | The current playback time in seconds | [Number] |

## Methods
| Name | Description | Returns |
| --- | --- | --- |
| play(time=0) | Plays the sound from `time` | [Promise] |
| playOnce(volume, time=0) | Plays the sound once from `time` with setting the volume to `volume`. Used for sound effects that can played at the same time. |  |
| resume | Shorthand for `sound.paused = false;` |  |

## Usage Example:
```javascript
import {sounds} from './Assets';
import Sound from './engine/Sound';

/*	
	path : String
			The string used for the <audio> element's src attribute
	loop : Boolean
			Should the sound be looped?
*/
let sound = new Sound(path, size);

sound.volume = 0.8;
sound.play();
```

<sub>See also [AudioElement], [String], [Boolean], [Number], [Promise]</sub>

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