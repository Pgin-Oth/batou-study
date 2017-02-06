from batou.component import Component
from batou.lib.file import File


class Tick(Component):

    def configure(self):
        self += File(
            'tick.sh',
            mode=0755,
            content="""\
#!/usr/bin/env bash
while true; do
  date
  sleep 1
done
""")