#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
from random import random
from operator import add
from paths import get_path
FILE_PATH = get_path(__file__)

def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 <= 1 else 0

def calculate_pi(sc=None, i=2):
    """
        Usage: pi [partitions]
    """

    sc.addPyFile(FILE_PATH)
    partitions = i
    n = 100000 * partitions
    count = sc.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    print(f"Pi is roughly {(4.0 * count / n)} with i={i}")
