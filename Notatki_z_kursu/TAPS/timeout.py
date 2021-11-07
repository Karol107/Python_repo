# import requests
#
# link = 'https://google.com'
# request_from_link = requests.get(link, timeout=1)
# # this causes the code to call a timeout if the connection or delays in
# # between the reads take more than 10 seconds
# print(request_from_link)

# url = 'https://google.com'
# start = time.clock()
# response = requests.post(url, data=post_fields, timeout=timeout)
# request_time = time.clock() - start
# self.logger.info("Request completed in {0:.0f}ms".format(request_time)
# #store request_time in persistent data store
import datetime
import datetime
import requests
# currDate = datetime.datetime.now()
# currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
# print(currDate)

import time

start = time.time()
print("hello")
time.sleep(5)
end = time.time()
print(int(end - start))