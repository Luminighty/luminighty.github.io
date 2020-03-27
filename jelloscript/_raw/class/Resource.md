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

!include _Links.md