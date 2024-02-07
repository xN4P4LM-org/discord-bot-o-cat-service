Create Discord Roles in this subdirectories to help bootstrapping a new server. The directory name will be the category type, and the corresponding .json file will be the role group including the group name and description.

An [example role](roles.json.example) is located in this directory.

For example, the following directory structure:

- `discord_roles/main`
  - `Location.json` - Where the user is located
  - `Gender.json` - The user's gender
- `discord_roles/optional`
  - `notifications.json` - relevant subscription to notifications
- `discord_roles/extra`
  - `hobbies.json` - The user's hobbies
- `discord_roles/special`
  - `color.json` - The user's favorite color
- etc...
