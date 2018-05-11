from strategy import Package


def deliver_package(package):
    if package.urgency == 'low':
        print('The', package.content, 'is going to be delivered by Bike')
        print('The cost will be $10')
        print('The ETA is 20 days')
    elif package.urgency == 'medium':
        print('The', package.content, 'is going to be delivered by Truck')
        print('The cost will be $30')
        print('The ETA is 13d ays')
    elif package.urgency == 'high':
        print('The', package. content, 'is going to be delivered by Plane')
        print('The cost will be $60')
        print('The ETA is 2 days')


package = Package('Racket', 'low')
deliver_package(package)
