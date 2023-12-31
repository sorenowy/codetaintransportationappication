#!/bin/bash

echo '==========================================='
echo 'INITIALIZE MIGRATIONS'
echo '==========================================='
prisma migrate deploy --schema ./app/database/prisma/schema.prisma
echo '###########################################'

echo '==========================================='
echo 'GENERATE TABLES'
echo '==========================================='
prisma generate --schema ./app/database/prisma/schema.prisma
echo '###########################################'

echo '==========================================='
echo 'START API SERVER'
echo '==========================================='
uvicorn main:app --host 0.0.0.0 --port 8000
echo '###########################################'
echo '♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥ ♥♥♥♥♥♥  ♥♥    ♥♥ ♥♥♥♥♥♥♥ ♥♥♥♥♥♥      ♥♥ ♥♥♥♥♥♥♥     ♥♥♥♥♥♥  ♥♥    ♥♥ ♥♥♥    ♥♥ ♥♥♥    ♥♥ ♥♥ ♥♥♥    ♥♥  ♥♥♥♥♥♥  '
echo '♥♥      ♥♥      ♥♥   ♥♥ ♥♥    ♥♥ ♥♥      ♥♥   ♥♥     ♥♥ ♥♥          ♥♥   ♥♥ ♥♥    ♥♥ ♥♥♥♥   ♥♥ ♥♥♥♥   ♥♥ ♥♥ ♥♥♥♥   ♥♥ ♥♥       '
echo '♥♥♥♥♥♥♥ ♥♥♥♥♥   ♥♥♥♥♥♥  ♥♥    ♥♥ ♥♥♥♥♥   ♥♥♥♥♥♥      ♥♥ ♥♥♥♥♥♥♥     ♥♥♥♥♥♥  ♥♥    ♥♥ ♥♥ ♥♥  ♥♥ ♥♥ ♥♥  ♥♥ ♥♥ ♥♥ ♥♥  ♥♥ ♥♥   ♥♥♥ '
echo '     ♥♥ ♥♥      ♥♥   ♥♥  ♥♥  ♥♥  ♥♥      ♥♥   ♥♥     ♥♥      ♥♥     ♥♥   ♥♥ ♥♥    ♥♥ ♥♥  ♥♥ ♥♥ ♥♥  ♥♥ ♥♥ ♥♥ ♥♥  ♥♥ ♥♥ ♥♥    ♥♥ '
echo '♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥ ♥♥   ♥♥   ♥♥♥♥   ♥♥♥♥♥♥♥ ♥♥   ♥♥     ♥♥ ♥♥♥♥♥♥♥     ♥♥   ♥♥  ♥♥♥♥♥♥  ♥♥   ♥♥♥♥ ♥♥   ♥♥♥♥ ♥♥ ♥♥   ♥♥♥♥  ♥♥♥♥♥♥  '
echo '###########################################'                                                                                                           