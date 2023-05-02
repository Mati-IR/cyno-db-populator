from rest_framework.routers import SimpleRouter

router = SimpleRouter()

# TODO: add here your API URLs
router.register(r'owners', OwnerViewSet)
router.register(r'dogs', DogViewSet)
router.register(r'championsship', ChampionshipViewSet)

urlpatterns = router.urls

