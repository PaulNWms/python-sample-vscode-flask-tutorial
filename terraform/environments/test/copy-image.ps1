$sourceImgVer = Get-AzGalleryImageVersion `
   -GalleryImageDefinitionName 'wiggly-image' `
   -GalleryName 'wigglyGallery' `
   -ResourceGroupName 'wiggly-world' `
   -Name 0.0.1
   
Get-AzGalleryImageDefinition `
   -GalleryName 'wigglyGallery' `
   -ResourceGroupName 'wiggly-world' `
   -Name 'wiggly-image'
   
$destinationImgDef  = New-AzGalleryImageDefinition `
   -GalleryName 'tstateGallery' `
   -ResourceGroupName 'tstate' `
   -Location 'WestUS2' `
   -Name 'wiggly-image' `
   -OsState specialized `
   -OsType Linux `
   -HyperVGeneration v1 `
   -Publisher 'Canonical' `
   -Offer 'UbuntuServer' `
   -Sku '16.04-LTS'
   
$region1 = @{Name='West US 2';ReplicaCount=1}
$targetRegions = @($region1)

$job = $imageVersion = New-AzGalleryImageVersion `
   -GalleryImageDefinitionName $destinationImgDef.Name`
   -GalleryImageVersionName '0.0.1' `
   -GalleryName 'tstateGallery' `
   -ResourceGroupName 'tstate' `
   -Location WestUS2 `
   -TargetRegion $targetRegions  `
   -Source $sourceImgVer.Id.ToString() `
   -PublishingProfileEndOfLifeDate '2021-12-01' `
   -asJob
   
Get-AzGalleryImageDefinition `
   -GalleryName 'tstateGallery' `
   -ResourceGroupName 'tstate' `
   -Name 'wiggly-image'