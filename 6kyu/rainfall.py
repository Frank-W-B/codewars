import pandas as pd
import numpy as np
data = """
Rome:Jan 81.2,Feb 63.2,Mar 70.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,Aug 27.5,Sep 60.9,Oct 117.7,Nov 111.0,Dec 97.9
London:Jan 48.0,Feb 38.9,Mar 39.9,Apr 42.2,May 47.3,Jun 52.1,Jul 59.5,Aug 57.2,Sep 55.4,Oct 62.0,Nov 59.0,Dec 52.9
Paris:Jan 182.3,Feb 120.6,Mar 158.1,Apr 204.9,May 323.1,Jun 300.5,Jul 236.8,Aug 192.9,Sep 66.3,Oct 63.3,Nov 83.2,Dec 154.7
NY:Jan 108.7,Feb 101.8,Mar 131.9,Apr 93.5,May 98.8,Jun 93.6,Jul 102.2,Aug 131.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2
Vancouver:Jan 145.7,Feb 121.4,Mar 102.3,Apr 69.2,May 55.8,Jun 47.1,Jul 31.3,Aug 37.0,Sep 59.6,Oct 116.3,Nov 154.6,Dec 171.5
Sydney:Jan 103.4,Feb 111.0,Mar 131.3,Apr 129.7,May 123.0,Jun 129.2,Jul 102.8,Aug 80.3,Sep 69.3,Oct 82.6,Nov 81.4,Dec 78.2
Bangkok:Jan 10.6,Feb 28.2,Mar 30.7,Apr 71.8,May 189.4,Jun 151.7,Jul 158.2,Aug 187.0,Sep 319.9,Oct 230.8,Nov 57.3,Dec 9.4
Tokyo:Jan 49.9,Feb 71.5,Mar 106.4,Apr 129.2,May 144.0,Jun 176.0,Jul 135.6,Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4
Beijing:Jan 3.9,Feb 4.7,Mar 8.2,Apr 18.4,May 33.0,Jun 78.1,Jul 224.3,Aug 170.0,Sep 58.4,Oct 18.0,Nov 9.3,Dec 2.7
Lima:Jan 1.2,Feb 0.9,Mar 0.7,Apr 0.4,May 0.6,Jun 1.8,Jul 4.4,Aug 3.1,Sep 3.3,Oct 1.7,Nov 0.5,Dec 0.7
"""

data1 = """
Rome:Jan 90.2,Feb 73.2,Mar 80.3,Apr 55.7,May 53.0,Jun 36.4,Jul 17.5,Aug 27.5,Sep 60.9,Oct 147.7,Nov 121.0,Dec 97.9
London:Jan 58.0,Feb 38.9,Mar 49.9,Apr 42.2,May 67.3,Jun 52.1,Jul 59.5,Aug 77.2,Sep 55.4,Oct 62.0,Nov 69.0,Dec 52.9
Paris:Jan 182.3,Feb 120.6,Mar 188.1,Apr 204.9,May 323.1,Jun 350.5,Jul 336.8,Aug 192.9,Sep 66.3,Oct 63.3,Nov 83.2,Dec 154.7
NY:Jan 128.7,Feb 121.8,Mar 151.9,Apr 93.5,May 98.8,Jun 93.6,Jul 142.2,Aug 131.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2
Vancouver:Jan 155.7,Feb 121.4,Mar 132.3,Apr 69.2,May 85.8,Jun 47.1,Jul 31.3,Aug 37.0,Sep 69.6,Oct 116.3,Nov 154.6,Dec 171.5
Sydney:Jan 123.4,Feb 111.0,Mar 151.3,Apr 129.7,May 123.0,Jun 159.2,Jul 102.8,Aug 90.3,Sep 69.3,Oct 82.6,Nov 81.4,Dec 78.2
Bangkok:Jan 20.6,Feb 28.2,Mar 40.7,Apr 81.8,May 189.4,Jun 151.7,Jul 198.2,Aug 197.0,Sep 319.9,Oct 230.8,Nov 57.3,Dec 9.4
Tokyo:Jan 59.9,Feb 81.5,Mar 106.4,Apr 139.2,May 144.0,Jun 186.0,Jul 155.6,Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4
Beijing:Jan 13.9,Feb 14.7,Mar 18.2,Apr 18.4,May 43.0,Jun 88.1,Jul 224.3,Aug 170.0,Sep 58.4,Oct 38.0,Nov 19.3,Dec 2.7
Lima:Jan 11.2,Feb 10.9,Mar 10.7,Apr 10.4,May 10.6,Jun 11.8,Jul 14.4,Aug 13.1,Sep 23.3,Oct 1.7,Nov 0.5,Dec 10.7
"""

towns = ["Rome", "London", "Paris", "NY", "Vancouver", "Sydney", "Bangkok", "Tokyo",
         "Beijing", "Lima", "Montevideo", "Caracas", "Madrid", "Berlin"]


#### Code wars submitted solution
import pandas as pd
import numpy as np

def parse_data(data_r):
    '''Parses raw data into a pandas dataframe'''
    lines = data_r.split('\n')
    cities = [] 
    rainfall_by_city = [] 
    for line in lines:
        if len(line) > 1:
            city = line.split(':')[0]
            cities.append(city) 
            month_rainfalls = line.split(':')[1]
            month_rainfall = month_rainfalls.split(',')
            months = [m_r.split(' ')[0] for m_r in month_rainfall]
            rainfall = np.array([m_r.split(' ')[1] for m_r in month_rainfall]).astype(float)
            rainfall_by_city.append(rainfall)
    columns = months
    index = cities
    df = pd.DataFrame(columns=columns, index = cities, data=rainfall_by_city)
    return df

def mean(town, strng):
    '''Returns the mean rainfall for the city'''
    df = parse_data(strng)
    means = df.mean(axis=1)
    if town in df.index:
        return means.loc[town]
    else:
        return -1

def variance(town, strng):
    ''' Returns the rainfall variance for the city'''
    df = parse_data(strng)
    var = df.var(axis=1, ddof=0)
    if town in df.index:
        return var.loc[town]
    else:
        return -1

### CW best practice/interesting solution:
import statistics, re

rain = lambda town, strng: map(float, re.findall("\d+(?:\.\d+)?", "".join(re.findall(town+":(.+)\n", strng))))

def mean_bp(town, strng):
    return statistics.mean(rain(town, strng))
def variance_bp(town, strng):
    return statistics.pvariance(rain(town, strng))


if __name__ == '__main__':
    #assertFuzzyEquals(mean("London", data), 51.199999999999996) 
    #assertFuzzyEquals(mean("Beijing", data), 52.416666666666664)
    #
    #Test.describe("variance data")
    #Test.it("Basic tests")
    #assertFuzzyEquals(variance("London", data), 57.42833333333374)
    #assertFuzzyEquals(variance("Beijing", data), 4808.37138888889)
    town = 'London'
    data = data
    ## mine 
    print("City: {0}, mean rainfall: {1}".format(town, mean(town, data)))
    print("City: {0}, rainfall var : {1}".format(town, variance(town, data)))
    ## best practice
    print("City: {0}, mean rainfall: {1}".format(town, mean_bp(town, data)))
    print("City: {0}, rainfall var : {1}".format(town, variance_bp(town, data)))
