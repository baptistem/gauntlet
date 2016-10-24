Gauntlet is a CLI password manager oriented multi-user.
The goal is to provide a solution for password in enterprise context.

_require : python3, gnugp, tk_

# usage
python3 gauntlet.py -s
you need to first to select the key with the option 1
otherwise everything else might fail


# curent version
v0.1.1
* failsafe

# coming next:
V0.1 Single User release
* encrypt password using own GPG key
* decrypt password using own GPG key
* add to clipboard for 10 secs

v0.2 Multi Uesr release
* encrypt key using other GPG key
* create an export file with password encrypted matching other GPG key
* merge json file (no strategy, data might be overriden)

v0.3 Server mode release
* add server mode
* client can ask for an id
* server will only consider signed request
* if the client is authorized, the server will answer the encrypted data
* add "state of live" for password : ok/old/nok

v0.4 Shiny release
* send a mail when a password reach old
* send a mail when a new password is saved
* generate password
* ...

