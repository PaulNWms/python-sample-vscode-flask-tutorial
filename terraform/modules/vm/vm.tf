resource "azurerm_network_interface" "test" {
  name                = "${var.application_type}-${var.resource_type}-nic"
  location            = var.location
  resource_group_name = var.resource_group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_address_id
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  prevent_destroy     = true
  name                = "${var.application_type}-${var.resource_type}"
  location            = var.location
  resource_group_name = var.resource_group
  size                = "Standard_B1s"
  admin_username      = "adminuser"
  network_interface_ids = [
    azurerm_network_interface.test.id,
  ]
  source_image_id = "/subscriptions/382e9492-020f-4300-b96a-8e5b88fc422a/resourceGroups/tstate/providers/Microsoft.Compute/images/wiggly-vm-image"
  admin_ssh_key {
    username   = "adminuser"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0Ol53Rp9MoyCRrcXwpuHbSXpvvHNT24dMy3NCnL8OD5bc2ywBMmAZAvc0BQoBZ8MxL9O67oaPENA/+C1UojdtHSyBfYXYZxRKiqFyrRTdYCqcFZ/brZfCxIeQJ7FWs5TKA2/CRMaudClnwZrrpKe8ihZyjEOyHT7AK3tHD00ixFnJ6M6WPwEEaRg0ZHMkrDKLa4+ikgg6d+cwWN80YJvpJUKgR+Qss7SD4aKI8lsXUf7KWNQgfGoppcAIdOpt95VFxUF5WzCNn8JT4a0xQdijftfeOgno2F7MITI3DLz3enk1Q4Ieo7nTxCnDM8KQUB+M0FDhQ6Tr6HQPEPKV75Cd"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  tags = {
    "project" = "quality-releases"
  }
}
