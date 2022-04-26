import dns.message as message
import dns.query as query
import dns.exception as exception
import time


def mydig(qname):
    startTime = time.time()
    root = '192.58.128.30'
    send = message.make_query(qname, "A")
    recv = query.tcp(send, root)
    # Get answer part from the receiving message
    answer = recv.sections[1]

    # answer = [] means the query is not end, still need to send query
    while not answer:
        try:
            ip_flag = False
            now = time.time()
            duration = now - startTime
            if duration < 0:
                if duration < -1:
                    raise exception.Timeout
                else:
                    now = startTime
            if duration > 2:
                raise exception.Timeout

            # get new ip in the receiving message section
            for ip in recv.sections[3]:
                ip_info = ip.to_text().split()
                ip_type = ip_info[3]

                # check if the type is 'A', get first ip_address in type 'A'
                if ip_type == "A":
                    new_ip = ip_info[4]
                    ip_flag = True
                    break
                else:
                    continue

            # get an 'A' type ip_address
            if ip_flag:
                recv = query.tcp(send, new_ip)
                answer = recv.sections[1]
                # check if the query end
                if answer:
                    answer_type = answer[0].to_text().split()[3]
                    # when answer_type is 'A' means the query end
                    if answer_type == "A":
                        return answer[0].to_text().split()
                    # when the answer is in a 'CNAME' type,
                    # we need use the 'CNAME' type domain making new query to the root.
                    if answer_type == "CNAME":
                        cname = answer[0].to_text().split()[4]
                        return mydig(cname)
            else:
                if recv.sections[2]:
                    cname = recv.sections[2][0].to_text().split()[4]
                    return mydig(cname)
        except exception.Timeout:
            print("Timeout!")


if __name__ == '__main__':
    domain = input("Input the name of domain you want to resolve: ")
    #domain = 'goole.com'
    start = time.ctime()
    start_time = time.time()
    output = mydig(domain)
    end_time = time.time()
    query_time = str((end_time - start_time) * 1000)
    print("Question Section: ")
    print(f"{domain:<26}" + f"{output[2]:<5}" + output[3])
    print()
    print("Answer Section: ")
    print(f"{domain:<16}" + f"{output[1]:<10}" + f"{output[2]:<5}" + f"{output[3]:<5}" + output[4])
    print()
    print("Query time: " + query_time)
    print("When: " + str(start))
