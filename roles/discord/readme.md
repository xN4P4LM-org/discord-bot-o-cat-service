Create your roles here in subdirectories. The directory name will be the category name, and the corresponding .json file will be the role name.

An [example role](../roles/roles.json.example) is located in the [`roles`](../roles/) directory.

For example, the following directory structure:

- `roles/main`
  - `Location.json` - Where the user is located
  - `Gender.json` - The user's gender
- `roles/optional`
  - `notifications.json` - relevant subscription to notifications
- `roles/extra`
  - `hobbies.json` - The user's hobbies
- `roles/special`
  - `color.json` - The user's favorite color
- etc...
