from strategy import Package


def bike_deliver(package):
    print('The', package.content, 'is going to be delivered by Bike')
    print('The cost will be $10')
    print('The ETA is 20 days')


def truck_deliver(package):
    print('The', package.content, 'is going to be delivered by Truck')
    print('The cost will be $30')
    print('The ETA is 13 days')


def plane_deliver(package):
    print('The', package.content, 'is going to be delivered by Plane')
    print('The cost will be $60')
    print('The ETA is 2 days')


def get_strategy(package):
    if package.urgency == 'low':
        strategy = bike_deliver
    if package.urgency == 'medium':
        strategy = truck_deliver
    if package.urgency == 'high':
        strategy = plane_deliver

    return strategy


package = Package('Computer', 'low')
deliver = get_strategy(package)
deliver()
