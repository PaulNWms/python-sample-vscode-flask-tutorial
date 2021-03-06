﻿#Provide the subscription Id of the subscription where managed disk exists
$sourceSubscriptionId='382e9492-020f-4300-b96a-8e5b88fc422a'

#Provide the name of your resource group where managed disk exists
$sourceResourceGroupName='wiggly-world'

#Provide the name of the managed disk
$managedDiskName='wiggly-vm_OsDisk_1_7b7a4edf929d48d492302d62ab246ecf'

#Set the context to the subscription Id where Managed Disk exists
Select-AzSubscription -SubscriptionId $sourceSubscriptionId

#Get the source managed disk
$managedDisk= Get-AzDisk -ResourceGroupName $sourceResourceGroupName -DiskName $managedDiskName

#Provide the subscription Id of the subscription where managed disk will be copied to
#If managed disk is copied to the same subscription then you can skip this step
$targetSubscriptionId='382e9492-020f-4300-b96a-8e5b88fc422a'

#Name of the resource group where snapshot will be copied to
$targetResourceGroupName='tstate'

#Set the context to the subscription Id where managed disk will be copied to
#If snapshot is copied to the same subscription then you can skip this step
Select-AzSubscription -SubscriptionId $targetSubscriptionId

$diskConfig = New-AzDiskConfig -SourceResourceId $managedDisk.Id -Location $managedDisk.Location -CreateOption Copy 

#Create a new managed disk in the target subscription and resource group
New-AzDisk -Disk $diskConfig -DiskName $managedDiskName -ResourceGroupName $targetResourceGroupName