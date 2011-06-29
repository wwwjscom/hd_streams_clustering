'''
Created on Jun 22, 2011

@author: kykamath
'''
from library.classes import Settings
from datetime import timedelta
from library.math_modified import getLargestPrimeLesserThan

twitterDataFolder='/mnt/chevron/kykamath/data/twitter/'
twitter_stream_settings = Settings(
                                   max_dimensions=99991, # Number of maximum dimensions to consider at a time. Make sue this is prime. This is also equal to the number of top phrases that will be considered for crowd discovery.
                                   min_phrase_length=2, # Minumum lenght of phrases. For example min_phrase_length=1 and max_phrase_length=1 will result in only unigrams as features.
                                   max_phrase_length=4, # Maximum lenght of phrases. For example min_phrase_length=1 and max_phrase_length=2 will result in both unigrams and bigrams as features.
                                   
                                   phrase_decay_coefficient=0.75, # The rate at which phrases decays.
                                   stream_decay_coefficient=0.75, # The rate at which stream decays.
                                   stream_cluster_decay_coefficient=0.5, # The rate at which a cluster decays.
                                   
                                   time_unit_in_seconds=timedelta(seconds=5*60), # This value will be used to determine the length of unit time intervals.
                                   
                                   dimension_update_frequency_in_seconds=timedelta(seconds=2*60*60), # Every these many seconds, old phrases are pruned and new dimensions are created.
                                   max_phrase_inactivity_time_in_seconds=timedelta(seconds=30*60), # Time after which a phrase can be considered old and need not be tracked.
                                   
                                   # Cluster pruning properties.
                                   cluster_filter_attribute = 'length', # The attribute based on which stream clusters will be pruned. 'length' => Size of clusters; score => streaming cluster score.
                                   cluster_filter_threshold = 5, # Value for the cluster filter threshold. All clusters with attribute values below this will be pruned.
                                   
                                   # Expert users data
                                   twitterUsersTweetsFolder='%susers/tweets/'%twitterDataFolder,
                                   usersToCrawl='%susers/crawl/users_to_crawl'%twitterDataFolder,
                                   )

# Streaming LSH clustering specific settings.
twitter_stream_settings.update(Settings(
                                dimensions=twitter_stream_settings.max_dimensions,
                                signature_length=23,
                                number_of_permutations=13,
                                threshold_for_document_to_be_in_cluster=0.1
                                ))

if __name__ == '__main__':
    print getLargestPrimeLesserThan(23)