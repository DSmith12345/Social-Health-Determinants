# Social-Health-Determinants

The goal of this project is to have python code that can obtain and store SDoH data for analysis.

## Application Examples

SDoH measures can be used to identify differences between patients that would normally have identical health profiles. This additional information can be used to predict the difference in health care costs.  
Source: https://carrothealth.com/carrot-health-insights-tale-two-patients/

With the used of SDoH measures it is possible to make predictions how certain regions will utilize Medicare plans that are available to them.  
Source: https://carrothealth.com/predicting-medicare-plan-choice/

Identifying SDoH that cause higher emergency department usage in certain areas.  
Source: https://carrothealth.com/call-me-a-doctor/

Having standardized data can help improve health services in many ways, some examples are improving health, lower costs, and linking patients to community services.  
Source: https://www.healthcatalyst.com/insights/social-determinants-health-todays-data-imperative

Assessing the capacity of social determinants of health data to augment predictive models identifying patients in need of wraparound social services.  
Source: https://academic.oup.com/jamia/article-abstract/25/1/47/4645255  

## References
Census data package provides an array of functions to help access Census Bureau data.
General information about the package can be found where: https://pypi.org/project/CensusData/
For more detailed documentation please refer to: https://jtleider.github.io/censusdata/ 

Pandas is a package that allows for data shaping and analysis.
For more information about Pandas visit: https://pandas.pydata.org/

Technical documentation for ACS-1 and ACS-5:
https://www.census.gov/programs-surveys/acs/technical-documentation/summary-file-documentation.html
Appendices for each include table number, table topic, geography restrictions, summary file sequence number,
summary file starting and ending positions, topics, and universe. 

The countypov function takes in a integer StateNum which is used to call the poverty data for the 
corresponding state's counties. After this the function returns a data frame with the county poverty data.

The tractpov function takes in a integer StateNum which is used to call the poverty data for the 
corresponding state's census tracts. After this the function returns a data frame with the tract poverty data.
Note state numbers do not match with the Census Bureau state numbers, to find the numbers use:
censusdata.geographies(censusdata.censusgeo([('state', '*')]), 'acs5', 2018) 

## Potential Futue SDoHs

#List of potential SDoH.

Determinants:
Social
1.Availability of resources to meet daily needs
  -Safe Housing
    ~Quality of Housing
  -Local Food Markets
  -Foods that Support Healthy Eating Patterns
2.Access to educational opportunities
  -Early Childhood Education and Development
  -Enrollment in Higher Education
  -High School Graduation
  -Health Literacy
3.Language/Literacy
  -English proficiency
4.Access to economic opportunities
5.Economic Stability
  -Employment
  -Food Insecurity
  -Housing Instability
  -Poverty
  -Cost of living
  -Income Level
6.Access to job opportunities
7.Access to health care services
  -Access to Primary Care
7.Quality of education
8.Quality of job training
9.Availability of community-based resources in support of community living
  -Opportunities for recreational
  -Leisure-time activities
10.Transportation options
11.Public safety
12.Social support
  -Access to consoling
  -Social isolation
13.Social and Community Context
  -Civic Participation
  -Incarceration
  -Social Cohesion
14.Social norms and attitudes 
  -Discrimination
  -Racism
  -Distrust of government
15.Exposure to crime, violence, and social disorder
  -Presence of trash
  -Lack of cooperation in a community
  -Domestic violence
16.Socioeconomic conditions
  -Concentrated poverty and the stressful conditions that accompany it
17.Residential segregation
18.Access to mass media and emerging technologies
  -Cell phones
  -The Internet
  -Social media
19.Culture

Physical
1.Natural environment
  -Green space 
    ~Grass
    ~Trees
  -weather 
    ~Climate change
2.Built environment
  -Buildings
  -Sidewalks
  -Bike lanes
  -Roads
3.Worksites
4.Schools
5.Recreational settings
4.Housing and community design
5.Exposure to toxic substances and other physical hazards
  -Air Pollution
6.Physical barriers
  -People with disabilities
7.Aesthetic elements
  -Good lighting
  -Trees
  -Benches


Sources:
1.HealthyPeople-https://www.healthypeople.gov/2020/topics-objectives/topic/social-determinants-of-health
2.CDC-https://www.cdc.gov/socialdeterminants/
3.WHO-https://www.who.int/social_determinants/en/
4.AHRQ-https://www.ahrq.gov/sdoh/index.html
